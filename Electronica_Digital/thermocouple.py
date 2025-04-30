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
        
        response = list(response)
        print(f"[INFO] Response: {response}")
        
        byte_high = response[0]<<8 #'<<' Correr 8 posiciones a la derecha (agrega 8 0's a la derecha del numero)
        byte_low = response[1]
        bin_response = byte_high + byte_low
        bin_response = bin_response>>3 #Agrega ceros a la izquierda lo que corre el numero a la derecha
        
        temperature = bin_response/4
        print(f"[INFO] Temperature: {temperature}")
        
        
        
if __name__ == "__main__":
    sensor = Thermocouple()
    while True:
        sensor.measure()