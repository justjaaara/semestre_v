from machine import Pin, Timer
import time
import _thread

class Pluviometer:
    
    def __init__(self, input_pin_number = 16):
        self.counter = 0
        self.input_pin_number = input_pin_number
        self.input_pin = Pin(self.input_pin_number, Pin.IN, pull = Pin.PULL_DOWN)
        self.input_pin.irq(handler = self.edge_detected, trigger = Pin.IRQ_RISING)
        self.run = True
        self.tim = Timer(0)
        self.tim_rain = Timer(1)
        self.tim_rain.init(mode = Timer.PERIODIC, period = 10000, callback = self.calculate_rain)
        
    def calculate_rain(self,tim_rain):
        self.rain = 0.2 * self.counter
        print(f"[INFO] Rainfall: {self.rain} mm/10s")
        self.counter = 0
        
    def edge_detected(self, pin_value):
        self.tim.init(mode = Timer.ONE_SHOT, period = 300, callback = self.count_pulse)
        
    def count_pulse(self, tim):
        self.counter += 1
        print(f"[INFO] {self.counter}")


if __name__ == "__main__":
    pluviometer = Pluviometer()
    
    try:
        
        while True:
            #led.blink() -> No hay que llamarlo porque está ejcutandose de manera paralela en otro hilo
            #print("[INFO] New iteration")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Murio")
    finally:
        print("[MESSAGE] Chao pescao")
            
    
