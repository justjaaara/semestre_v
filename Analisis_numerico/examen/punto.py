import matplotlib.pyplot as plt

# Parámetros del problema
m = 0.11  
g = 9.8  
k = 0.002 
h = 0.1   
t0 = 0    
tf = 6    
v0 = 8    

tiempos = [t0]
velocidades = [v0]
posiciones = [0]  # Posición inicial

while t0 < tf and posiciones[-1] >= 0:  # Detenemos cuando el proyectil toca el suelo
    t0 += h
    velocidades.append(velocidades[-1] + h * (-g - (k/m) * velocidades[-1] * abs(velocidades[-1])))
    posiciones.append(posiciones[-1] + h * velocidades[-1])
    tiempos.append(t0)

# Grafica velocidad vs tiempo
plt.plot(tiempos, velocidades, label="Velocidad (m/s)", color="blue")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.title("Velocidad del proyectil vs Tiempo")
plt.show()

# Encontrar el tiempo en que alcanza la altura máxima (cuando v cambia de signo)
t_max = None
for i in range(len(velocidades)):
    if velocidades[i] <= 0:  # La velocidad se vuelve cero o negativa
        t_max = tiempos[i]
        break  # Detenemos la búsqueda al encontrar el primer valor

# Encontrar el tiempo de impacto con el suelo
t_impact = tiempos[len(tiempos) - 1]
print(f"El proyectil alcanza la altura máxima en t aproximadamente {t_max} s")
print(f"El proyectil impacta el suelo en t aproximadamente {t_impact} s")
