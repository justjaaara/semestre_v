# Ejercicio catcher

from ceros import Biseccion
import numpy as np


x = 35
g = 9.8
vo = 20
yo = 2
y =1
f_trayectoria = lambda theta: 35 *np.tan(theta)-((g)*(x**2))/((2)*(vo**2)*(np.cos(theta))**2)+yo-y

iteracion_theta, theta_inicial = (Biseccion(f_trayectoria,0,np.pi/4,1e-6))
print(f"El ángulo inicial es: {np.degrees(theta_inicial)} y en {iteracion_theta} iteraciones se encontró la solución")