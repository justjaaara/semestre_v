from machine import UART
import time


uart = UART(2,9600) #9600 bits por segundo de informacion
counter = 0
while True:
    """
    Sentido Microcontrolador -> Pc
    counter_str = f"{counter}"
    counter += 1
    uart.write(counter_str)
    time.sleep(1)
    """
    # Sentido Pc -> Microcontrolador
    characters = uart.any()
    if character != 0:
        msg = uart.read()
        print(f"[INFO] Message received: {msg}")
              
    time.sleep(1)
    
    