from machine import Pin, Timer
import time
import _thread

class SensorUltrasonico:
    def __init__(self, trigger_pin_number=26, echo_pin_number=27,
                 sensor_min=10.90, real_min=10, sensor_max=99.16, real_max=100):
        self.tank_height = 100
        self.trigger = Pin(trigger_pin_number, Pin.OUT)
        self.echo = Pin(echo_pin_number, Pin.IN)
        self.distance = 0
        self.m = (real_max - real_min) / (sensor_max - sensor_min)
        self.b = real_min - self.m * sensor_min
        _thread.start_new_thread(self.update_distance, ())

    def calibrate_distance(self, raw_distance):
        return self.m * raw_distance + self.b

    def measure_distance(self):
        self.trigger.off()
        time.sleep_us(2)
        self.trigger.on()
        time.sleep_us(10)
        self.trigger.off()

        timeout_us = 30000  # 30 ms

        start = time.ticks_us()
        while self.echo.value() == 0:
            if time.ticks_diff(time.ticks_us(), start) > timeout_us:
                return -1  

        t1 = time.ticks_us()
        while self.echo.value() == 1:
            if time.ticks_diff(time.ticks_us(), t1) > timeout_us:
                return -1 
        t2 = time.ticks_us()

        duration = time.ticks_diff(t2, t1)
        distance_in_cm = duration / 58.0

        if distance_in_cm < 0 or distance_in_cm > (self.tank_height + 20):
            return -1 

        return self.calibrate_distance(distance_in_cm)

    def update_distance(self):
        while True:
            try:
                new_distance = self.measure_distance()
                if new_distance != -1:
                    self.distance = new_distance
                time.sleep(0.5)
            except Exception as e:
                print(f"[ERROR] An Error occurred: {e}") 

    def get_current_level(self):
        nivel = self.tank_height - self.distance
        if nivel < 0:
            return 0
        elif nivel > self.tank_height:
            return self.tank_height
        return nivel


class ControlTanque:
    def __init__(self, fillling_btn_pin=13, draining_btn_pin=25, stop_all_btn_pin=32, filling_led_pin=14, draining_led_pin=12):
        self.sensor = SensorUltrasonico()
        self.min_level = 80
        self.max_level = 90
        self.stop_requested = False
        self.timer_bouncer = Timer(0)

        self.filling_active = False
        self.draining_active = False

        self.filling_button = Pin(fillling_btn_pin, Pin.IN, Pin.PULL_DOWN)
        self.draining_button = Pin(draining_btn_pin, Pin.IN, Pin.PULL_DOWN)
        self.stop_all_button = Pin(stop_all_btn_pin, Pin.IN, Pin.PULL_DOWN)

        self.filling_led = Pin(filling_led_pin, Pin.OUT)
        self.draining_led = Pin(draining_led_pin, Pin.OUT)

        self.filling_button.irq(trigger=Pin.IRQ_RISING, handler=self.bounce_controller)
        self.draining_button.irq(trigger=Pin.IRQ_RISING, handler=self.bounce_controller)
        self.stop_all_button.irq(trigger=Pin.IRQ_RISING, handler=self.stop_all)

    def handle_fill_btn(self, pin):
        if self.filling_active:
            print("[INFO] Filling process already active. Stopping...")
            self.stop_requested = True
            self.filling_active = False
            return
        else:
            _thread.start_new_thread(self.start_filling, ())

    def handle_drain_btn(self, pin):
        if self.draining_active:
            print("[INFO] Draining process already active. Stopping...")
            self.stop_requested = True
            self.draining_active = False
            return
        else:
            _thread.start_new_thread(self.start_draining, ())
    
    def bounce_controller(self, button_value):
        button_value_str = str(button_value)
        boton_pin_number = int(button_value_str[4:-1])
        action = None
        if boton_pin_number == 13:
            action = self.handle_fill_btn
        elif boton_pin_number == 25:
            action = self.handle_drain_btn
        elif boton_pin_number == 32:
            action = self.stop_all
        else:
            print("[ERROR] Pressed button has not been assigned to anything")
            return

        self.timer_bouncer.init(mode = Timer.ONE_SHOT, period = 300, callback = action)

    def start_filling(self):
        if self.draining_active:
            print("[INFO] Cannot fill while draining. Stop drain first.")
            return

        self.stop_requested = False
        self.filling_active = True
        print("[INFO] Starting filling...")

        while self.sensor.get_current_level() < self.max_level:
            if self.stop_requested:
                break
            print(f"[INFO] Filling tank, current level: {self.sensor.get_current_level()}")
            self.filling_led.value(1)
            time.sleep(0.2)

        self.filling_led.value(0)
        self.filling_active = False
        if not self.stop_requested:
            print("[INFO] Filling process completed.")

    def start_draining(self):
        if self.filling_active:
            print("[INFO] Cannot drain while filling. Stop fill first.")
            return

        self.stop_requested = False
        self.draining_active = True
        print("[INFO] Starting draining...")

        while self.sensor.get_current_level() > self.min_level:
            if self.stop_requested:
                break
            print(f"[INFO] Draining tank, current level: {self.sensor.get_current_level()}")
            self.draining_led.value(1)
            time.sleep(0.2)

        self.draining_led.value(0)
        self.draining_active = False
        if not self.stop_requested:
            print("[INFO] Draining process completed.")

    def stop_all(self, pin):
        if not self.filling_active and not self.draining_active:
            print("[INFO] There is no process to be stopped.")
        else:
            self.stop_requested = True
            self.filling_active = False
            self.draining_active = False
            self.filling_led.value(0)
            self.draining_led.value(0)
            print("[STOPPED] Process stopped by the user.")

        
if __name__ == "__main__":
    control = ControlTanque()

    while True:
        time.sleep(1)
        print("[INFO] Current level:", control.sensor.get_current_level(), "cm")
