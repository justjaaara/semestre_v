"""
Este código implementa el método de Jacobi con sumas para resolver sistemas de ecuaciones lineales.
"""
import numpy as np
import time

def jacobi_con_sumas(A, b, x0, n_max, tol):
    """
    -----------
    Parametros
    -----------
    - A: matriz de coeficientes cuadrada
    - b: vector de términos independientes
    - x0: vector inicial --> Si no me da el dato se asume que el vector es el vector nulo
    - n_max: número máximo de iteraciones
    - tol: Exactitud con la cual encontraremos la solución del sistema de ecuaciones lineales (SEL). Si no me dan este dato se asume que la tolerancia es 1e-6
    -----------
    Nota
    ------------
    - TANTO LA MATRIZ A COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
    - AMBAS TIENE QUE TENER DIAGONAL ESTRICTAMENTE DOMINANTE
    """

    n = len(b)  # -> Tamaño del vector b que es el mismo de A porque es cuadrada
    x1 = np.zeros(n)
    error = 10
    iteracion = 0
    
    #TODO: Medir el tiempo de cómputo del método
    
    time_start = time.time()
    while error > tol and iteracion < n_max:
        for i in range(n):
            suma = 0  # Inicializar suma para cada fila
            for j in range(n):
                if i != j:
                    suma += np.dot(A[i][j], x0[j])  # Acumular la suma correctamente
            x1[i] = (b[i] - suma) / A[i][i]
        
        # Calculo el error como la norma infinito de la diferencia
        error = np.max(np.abs(x1 - x0))
        
        # Actualizo el vector inicial
        x0 = np.copy(x1)
        iteracion += 1
        
        # print(f"Iteración {iteracion}: {x1}, Error: {error}")
    time_end = time.time()
    tiempo_total = time_end - time_start
    
    return x1, error, tiempo_total


A = np.array([[3, -1, 0], [-1, 4, -1], [0, -1, 5]], dtype=float)
b = np.array([2, 3, 5], dtype=float)
x0 = np.zeros(len(b), dtype=float)
n_max = 50
tol = 1e-6
solucion, error, tiempo_total = jacobi_con_sumas(A, b, x0, n_max, tol)
print("La solución es:", solucion)
print("El error es:", error)
print("El tiempo de cómputo es:", tiempo_total)
