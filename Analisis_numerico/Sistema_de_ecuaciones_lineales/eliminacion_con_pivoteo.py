import numpy as np

# Declarar la matriz A y el vector de términos independientes b

A = np.array([[0,2,1],[0,-8,-2],[1,-1,-2]])
b = np.array([2,1,3])

print(f"Matriz original A: \n{A}")
print(f"Vector b original: \n{b}")
print("-------------")
# Entradas tipo flotante
def eliminacion_gaussiana_piv(A, b):
    
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    for filas in range(n - 1):

        if abs(A[filas][filas]) < 1e-10:

            max_fila = np.argmax(abs(A[filas:, filas])) + filas
            A[[filas, max_fila]] = A[[max_fila, filas]]
            b[[filas, max_fila]] = b[[max_fila, filas]]

        for columnas in range(filas + 1, n):
            factor = A[columnas][filas] / A[filas][filas]
            A[columnas] = A[columnas] - factor * A[filas]
            b[columnas] = b[columnas] - factor * b[filas]
            print(factor)

    #Regresion hacia atras
    x = np.zeros(n)
    for k in range (n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:n], x[k+1:n])) / A[k,k]

    return x
        

# print("Solución del sistema de ecuaciones lineales:")
print(eliminacion_gauus_piv(A,b))