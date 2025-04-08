"""
Un tanque contiene 200 L de un líquido en el cual se disuelven 30 g de sal. Una salmuera que contiene 1g de sal por litro se bombea al tanque a razón de 4L/min; la solución, adecuadamente mezclada, se bombea hacia afuera con la misma rapidez.

dQdt+QVr2=Q1r1


donde Q, es la cantidad de sal en el tanque, r1,r2
, son las velocidades y (Q1
 es la concentración de entrada.

1. Encuentre el número de gramos de sal que hay en el tanque al cabo de 30 minutos.
2. Realice una gráfica de la cantidad de sal en cualquier instante t. (recomendación realice en un periodo de tiempo de [0, 1h])
"""
import matplotlib.pyplot as plt

# Parámetros
V = 200  
h=0.1
r1 = 4   
r2 = 4   
Q = 30
t0= 0
tf= 30

concentraciones = [1]
while (t0 < tf):
    t0+=h
    concentraciones.append(h*((concentraciones[-1]*r1) - ((Q/V)*r2))+concentraciones[-1])


plt.plot(concentraciones)
plt.xlabel('Tiempo (min)')
plt.ylabel('Cantidad de sal (g)')
plt.title('Cantidad de sal en el tanque en función del tiempo')
plt.grid(True)
plt.show()