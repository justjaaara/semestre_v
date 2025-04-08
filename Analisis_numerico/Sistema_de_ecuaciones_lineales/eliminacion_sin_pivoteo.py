"""
 Este solo funciona para matrices cuadradas y con diagonal dominante, es decir que 
    los elementos de la diagonal principal son mayores a la suma de los elementos de la fila
    o sea que no haya un 0 en la diagonal principal.
"""

import numpy as np

# Declarar la matriz A y el vector de términos independientes b

A = np.array([[-3,2,1],[6,-8,-2],[1,-1,-2]])
b = np.array([2,1,3])

# Entradas tipo flotante
def eliminacion_gauus(A,b):
    A = A.astype(float)
    b = b.astype(float)
    # print(A)
    # print("-------------")
    n = len(b) # -> longitud de la matriz
    for i in range(n-1):
        for j in range(i+1,n):
            factor_lambda = A[j,i]/A[i,i]
            A[j] = A[j] - factor_lambda * A[i]
            b[j] = b[j] - factor_lambda * b[i]
    # print(A)
    # print(b)
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n])) / A[k,k]
    return x

# print("Solución del sistema de ecuaciones lineales:")
print(eliminacion_gauus(A,b))