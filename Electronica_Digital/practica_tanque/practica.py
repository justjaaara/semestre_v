import time
from machine import Pin

# Definir los pines
trigger_pin = Pin(26, Pin.OUT)  # Pin 26 para el Trigger
echo_pin = Pin(27, Pin.IN)     # Pin 27 para el Echo

# Función para medir distancia
def medir_distancia():
    # Asegurarse de que el Trigger esté en bajo al inicio
    trigger_pin.value(0)
    time.sleep_us(2)

    # Enviar un pulso de 10us al pin Trigger
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    # Esperar la respuesta en el pin Echo
    timeout = time.ticks_ms() + 200  # Establecer un tiempo de espera de 200ms
    while echo_pin.value() == 0:
        if time.ticks_ms() > timeout:  # Si no se recibe la señal, consideramos que no hay objeto
            return 0  # No se recibe la señal de vuelta
    pulse_start = time.ticks_us()  # Tiempo de inicio del pulso

    timeout = time.ticks_ms() + 200  # Establecer un nuevo tiempo de espera para el pulso de retorno
    while echo_pin.value() == 1:
        if time.ticks_ms() > timeout:  # Si no se recibe la señal, consideramos que no hay objeto
            return 0  # No se recibe la señal de vuelta
    pulse_end = time.ticks_us()  # Tiempo de fin del pulso

    # Calcular el tiempo de vuelo
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)

    # Calcular la distancia (velocidad del sonido 343 m/s, o 0.0343 cm/us)
    distancia = (pulse_duration * 0.0343) / 2  # Dividido por 2 porque el pulso viaja hacia y regresa

    # Si la distancia es mayor que 400 cm, probablemente haya un error
    if distancia > 400:
        return 0  # Si la distancia es extremadamente grande, consideramos que no hay objeto

    return distancia

# Bucle principal
while True:
    distancia = medir_distancia()
    print("Distancia: {:.2f} cm".format(distancia))
    time.sleep(1)  # Esperar 1 segundo antes de la siguiente medición
