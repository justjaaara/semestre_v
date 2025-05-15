import ujson
import time
import _thread
from machine import ADC, Pin, UART, SoftSPI

class Thermocouple:
    def __init__(self, miso_pin=12, sck_pin=14, mosi_pin=13, chip_select_pin=15):
        self.bus = SoftSPI(sck=Pin(sck_pin), mosi=Pin(mosi_pin), miso=Pin(miso_pin))
        self.cs = Pin(chip_select_pin, Pin.OUT)
        self.cs.value(1)

    def read_temp(self):
        self.cs.value(1)
        time.sleep(1) 
        
        self.cs.value(0)
        time.sleep_us(1)  

        response = self.bus.read(2)
        time.sleep_us(1)
        self.cs.value(1)

        if response is None or len(response) != 2:
            print("[ERROR] Error de lectura SPI: respuesta inválida")
            return -1  

        response = list(response)

        byte_high = response[0] << 8
        byte_low = response[1]
        bin_response = byte_high + byte_low
        bin_response = bin_response >> 3

        temperature = bin_response / 4  # Cada unidad representa 0.25 °C
        return temperature


class GenericADC:
    def __init__(self, pin, scale=3.3, resolution=4095):
        self.adc = ADC(Pin(pin))
        self.adc.atten(ADC.ATTN_11DB)
        self.scale = scale
        self.resolution = resolution
        self.value = 0

    def read(self):
        raw = self.adc.read()
        voltage = (raw / self.resolution) * self.scale
        self.value = voltage
        return voltage

    def read_temp_lm35(self):
        voltage = self.read()
        return voltage * 100 

class LEDController:
    def __init__(self, config_path="config.json"):
        self.load_config(config_path)
        self.green = Pin(21, Pin.OUT)
        self.yellow = Pin(22, Pin.OUT)
        self.red_temp = Pin(23, Pin.OUT)
        self.blue_low_warning_led = Pin(2, Pin.OUT)

    def load_config(self, path):
            with open(path) as f:
                config = ujson.load(f)
                self.warning_level = config["warning_level"]
                self.emergency_level = config["emergency_level"]
                self.low_voltage_threshold = config["low_voltage_threshold"]
                self.sensor_source = config["sensor_source"]

    def update_leds(self, temp, voltage):
        if temp < self.warning_level:
            self.green.value(1)
            self.yellow.value(0)
            self.red_temp.value(0)
        elif self.warning_level <= temp < self.emergency_level:
            self.green.value(0)
            self.yellow.value(1)
            self.red_temp.value(0)
        else:
            self.green.value(0)
            self.yellow.value(0)
            self.red_temp.value(1)

        if voltage < self.low_voltage_threshold:
            self.blue_low_warning_led.value(1)
        else:
            self.blue_low_warning_led.value(0)

class UARTLogger:
    def __init__(self, tx=17, rx=16, baudrate=9600):
        self.uart = UART(1, tx=tx, rx=rx, baudrate=baudrate)

    def log(self, temp_lm35, voltage, temp_thermocouple):
        msg = ujson.dumps({
            "timestamp": time.time(),
            "LM35_temp": temp_lm35,
            "Thermocouple_temp": temp_thermocouple,
            "Voltage": voltage,
            "sensor_in_use": "LM35" if temp_lm35 else "Thermocouple"
        })
        self.uart.write("\n\r" + msg)

def adc_worker(adc_lm35, adc_voltage):
    while True:
        adc_lm35.read()
        adc_voltage.read()
        time.sleep(0.1)


def main():
    lm35 = GenericADC(pin=34)
    voltage = GenericADC(pin=35)
    thermocouple = Thermocouple()
    led_controller = LEDController()
    uart_logger = UARTLogger()

    _thread.start_new_thread(adc_worker, (lm35, voltage))

    print("Sistema de monitoreo de incubadora iniciado")

    while True:
        temp_lm35 = lm35.read_temp_lm35()
        voltage_val = voltage.value
        temp_tc = thermocouple.read_temp()

        if led_controller.sensor_source == "LM35":
            temp_to_use = temp_lm35
        else:
            temp_to_use = temp_tc

        led_controller.update_leds(temp_to_use, voltage_val)
        uart_logger.log(temp_lm35, voltage_val, temp_tc)

        print(f"LM35: {temp_lm35:.2f}°C | Termopar: {temp_tc:.2f}°C | Voltaje: {voltage_val:.2f}V")

        time.sleep(1)

if __name__ == "__main__":
    main()