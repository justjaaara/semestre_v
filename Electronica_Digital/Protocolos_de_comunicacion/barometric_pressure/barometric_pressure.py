from machine import SoftI2C, Pin
from bmp280 import *
import time
class Barometric_Pressure:
    
    def __init__(self, scl_pin_number = 22, sda_pin_number=21):
        self.bus = SoftI2C(scl = Pin(scl_pin_number), sda = Pin(sda_pin_number))
        print(self.bus.scan())
        self.sensor = BMP280(self.bus)
        
        bmp = BMP280(self.bus)
        bmp.use_case(BMP280_CASE_WEATHER)
        bmp.oversample(BMP280_OS_HIGH)

        bmp.temp_os = BMP280_TEMP_OS_8
        bmp.press_os = BMP280_PRES_OS_4

        bmp.standby = BMP280_STANDBY_250
        bmp.iir = BMP280_IIR_FILTER_2

        bmp.spi3w = BMP280_SPI3W_ON

        bmp.power_mode = BMP280_POWER_FORCED
        # or 
        bmp.force_measure()

        bmp.power_mode = BMP280_POWER_NORMAL
        # or 
        bmp.normal_measure()
        # also
        #bmp.in_normal_mode()

        bmp.power_mode = BMP280_POWER_SLEEP
        # or 
        bmp.sleep()
        
        self.sensor = bmp
        
    def read_temperature(self):
        return self.sensor.temperature
    
    def read_barometric_pressure(self):
        return self.sensor.pressure
    
if __name__ == "__main__":
    sensor = Barometric_Pressure()
    while True:
        print(f"[INFO] Temperature: {sensor.read_temperature()}C, Pressure: {sensor.read_barometric_pressure()}mmHg")
        time.sleep(1)

