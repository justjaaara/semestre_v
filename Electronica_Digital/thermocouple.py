from machine import SoftSPI, Pin
import time

class Thermocouple:
    def __init__(self, miso_pin = 12, sck_pin = 14, mosi_pin = 13, chip_select_pin = 15):
        self.miso_pin = miso_pin
        self.sck_pin = sck_pin
        self.mosi_pin = mosi_pin
        self.chip_select_pin = chip_select_pin
        self.bus = SoftSPI(sck = Pin(self.sck_pin), mosi = Pin(self.mosi_pin), miso = Pin(self.miso_pin))
        
        self.chip_select = Pin(self.chip_select_pin, Pin.OUT)
        self.chip_select.value(1)
        
    def measure(self):
        self.chip_select.value(1)
        time.sleep(1)
        self.chip_select.value(0)
        time.sleep(1e-6) # Esperar mil nanosegundos?
        response = self.bus.read(2)
        time.sleep(1e-6)
        self.chip_select.value(1)
        
        print(f"[INFO] Response: {response}")
        
if __name__ == "__main__":
    sensor = Thermocouple()
    while True:
        sensor.measure()