from machine import ADC, Pin
import time
import math

class Voltemeter:
    def __init__(self, adc_pin = 15, num_samples = 30, adc_min = 218, v_min = 0.273, adc_max = 2045, v_max = 1.735):
        self.adc_min = adc_min
        self.v_min = v_min
        self.adc_max = adc_max
        self.v_max = v_max
        self.num_samples = num_samples
        self.adc_pin = adc_pin
        self.adc = ADC(Pin(self.adc_pin))
        self.adc.atten(ADC.ATTN_11DB) # -> Definir el rango de medición en voltaje
        
    def scale(self, divisions):
        m = (self.v_max - self.v_min)/(self.adc_max-self.adc_min)
        b = self.v_min - (m * self.adc_min)
        voltage = m*divisions + b
        return voltage
                
    def measure(self):
        adc_samples = []
        for i in range(0, self.num_samples):
            adc_samples.append(self.adc.read())
            time.sleep(10e-3)
        adc_samples.sort()
        if (self.num_samples - 1) % 2 ==0:
            mitad_1 = ( self.num_samples - 1)//2
            mitad_2 = mitad_1 + 1
            divisions = (adc_samples[mitad_1] + adc_samples[mitad_2])/2
            return self.scale(divisions)
        else:
            divisions = adc_samples[self.num_samples//2]
            return self.scale(divisions)
    
if __name__ == "__main__":
    voltemeter = Voltemeter()
    while True:
        print(f"[INFO] Divisions: {voltemeter.measure()}")
        time.sleep(1)