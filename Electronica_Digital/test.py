from machine import Pin
import time

class ButtonHandler:
    
    def __init__(self):
        # === Pines de botones ===
        self.btn1 = Pin(13, Pin.IN, Pin.PULL_DOWN)  # G13
        self.btn2 = Pin(25, Pin.IN, Pin.PULL_DOWN)  # G25
        self.btn3 = Pin(32, Pin.IN, Pin.PULL_DOWN)  # G32
        
        # === Pines de LEDs ===
        self.led1 = Pin(12, Pin.OUT)  # LED asociado al botón 1
        self.led2 = Pin(14, Pin.OUT)  # LED asociado al botón 2

        # Inicialmente apagados
        self.led1.value(0)
        self.led2.value(0)
        
        # === Configurar interrupciones ===
        self.btn1.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_btn1)
        self.btn2.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_btn2)
        self.btn3.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_btn3)

    def handle_btn1(self, pin):
        if self.led1.value() == 1:
            self.led1.value(0)
        else:
            self.led1.value(1)
        print("[BOTÓN 1] Presionado (G13) → LED1 ENCENDIDO (G12)")

    def handle_btn2(self, pin):
        if self.led2.value() == 1:
            self.led2.value(0)
        else:
            self.led2.value(1)
        print("[BOTÓN 2] Presionado (G25) → LED2 ENCENDIDO (G14)")

    def handle_btn3(self, pin):
        self.led1.value(0)
        self.led2.value(0)
        print("[BOTÓN 3] Presionado (G32) → TODOS LOS LEDS APAGADOS")


if __name__ == "__main__":
    print("[INFO] Sistema de botones iniciado. Esperando acciones...")
    handler = ButtonHandler()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("[INFO] Interrupción manual.")
    finally:
        print("[FIN] Terminando programa.")
