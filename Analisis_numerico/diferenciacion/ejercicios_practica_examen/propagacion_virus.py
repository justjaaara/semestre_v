"""
Suponga que un alumno es portador del virus de la gripe y regresa a su escuela donde
hay 1000 estudiantes. Si se supone que la constante de proporción del modelo es
k = 0.0009906 con que se propaga al virus no sólo a la cantidad x de alumnos
infectados, sino también a la cantidad de alumnos no infectados, determinar la
cantidad de alumnos infectados seis días después
El modelo es :
dx/dt = kx (1000 − x )

Calcular la cantidad de contagiado al cabo de 6 días
Realizar una gráfica de la información de: los contagiados y los no contagiados.
"""
import matplotlib.pyplot as plt


infectados = [1]
poblacion = [999]
k = 0.0009906
t0= 0
h = 0.1
tf = 6

while (t0 < 6):
    t0+=h
    infectados.append(h*(k*infectados[-1]*(1000 - infectados[-1]))+infectados[-1])
    poblacion.append(1000 - infectados[-1])


print(infectados)

plt.plot(infectados)
plt.plot(poblacion)
plt.show()