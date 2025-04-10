# Ejemplo de programación funcional en Python
from functools import reduce

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Función para calcular el cuadrado de un número
def cuadrado(x):
    return x ** 2

# Usar map para aplicar la función cuadrado a cada elemento de la lista
cuadrados = list(map(cuadrado, numeros))
print("Cuadrados:", cuadrados)

# Usar filter para filtrar los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Números pares:", pares)

# Usar reduce para calcular la suma de todos los números
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)