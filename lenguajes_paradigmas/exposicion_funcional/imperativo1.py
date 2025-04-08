# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calcular los cuadrados usando un bucle for
cuadrados = []
for num in numeros:
    cuadrados.append(num ** 2)

# Filtrar los números pares usando un bucle for
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

# Calcular la suma total usando un bucle for
suma_total = 0
for num in numeros:
    suma_total += num

print("Cuadrados:", cuadrados)
print("Números pares:", pares)
print("Suma total:", suma_total)