import numpy as np
import matplotlib.pyplot as plt
m = 68.1
c = 15
g = 9.8
h= 0.1
velocidades = [0]
t0=0
tf=t0+h
velocidades_analiticas = [0]
errores_absolutos = []

while(tf < 120):
    velocidades.append((h*(g-((c/m)*velocidades[-1]))+velocidades[-1]))
    velocidades_analiticas.append(((g*m)/c)*(1-np.exp(-(c/m)*tf)))
    errores_absolutos.append(abs(velocidades_analiticas[-1]- velocidades[-1]))
    tf+=h



velocidad_analitica = velocidades_analiticas[-1]
velocidad_numerica = velocidades[-1]
error_a= abs(velocidad_analitica-velocidad_numerica)
print(error_a)
plt.plot(velocidades)
plt.plot(errores_absolutos)
plt.show()