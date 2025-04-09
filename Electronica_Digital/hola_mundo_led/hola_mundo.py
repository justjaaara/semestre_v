from machine import Pin
import time
import _thread

class Led:
    
    def __init__(self, pin_number = 17, blink_time = [1, 5], input_pin_number = 16):
        self.pin_number = pin_number
        self.blink_time = blink_time
        self.counter = 0
        self.input_pin_number = input_pin_number
        self.pin = Pin(self.pin_number, Pin.OUT)
        self.input_pin = Pin(self.input_pin_number, Pin.IN, pull = Pin.PULL_DOWN)
        self.input_pin.irq(handler = self.change_time, trigger = Pin.IRQ_RISING | Pin.IRQ_FALLING)
        self.position = 0
        self.run = True
        _thread.start_new_thread( self.blink, ())
        
    def change_time(self, pin_value):
        self.counter += 1
        print(f"[INFO] {self.counter}")
        
        if self.input_pin.value() == 0:
            self.position = 0
        else:
            self.position = 1
            
    def blink(self):
        while self.run: 
            print("[INFO] Blinking")
            self.pin.value(1)
            time.sleep(self.blink_time[self.position])
            print("[INFO] Blink off")
            self.pin.value(0)
            time.sleep(self.blink_time[self.position])


if __name__ == "__main__":
    led = Led()
    
    try:
        
        while True:
            #led.blink() -> No hay que llamarlo porque está ejcutandose de manera paralela en otro hilo
            print("[INFO] New iteration")
            time.sleep(5)
    except KeyboardInterrupt:
        led.run = False
    finally:
        print("[MESSAGE] Chao pescao")
            
    
