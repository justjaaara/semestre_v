# INCORRECTO

"""
(Crecimiento del cultivo de bacterias). Suponga que la población de una colonia de
bacterias crece de manera proporcional de 100 a la población en el tiempo t, que la
población inicial de bacterias fue de 1000.

1) cabo de 3 horas cuantas bacterias se detectan?
2) Realice la gráfica de la situación y compárela con la solución analítica
y después de tres horas de observación, desde el inicio del proceso, se detectan 2000
bacterias.
"""

import matplotlib.pyplot as plt
import numpy as np
poblacion_bacterias = [1000]

h= 0.1
t0 = 0
tf= 3
k = 0.231 # constante de proporcionalidad hallada utilizando calculo diferencial


while (t0 < tf):
    poblacion_bacterias.append(h*(1000*poblacion_bacterias[-1])+poblacion_bacterias[-1])
    t0 += h

print(poblacion_bacterias[-1])
plt.plot(poblacion_bacterias)
plt.show()

