"""
This module implements the secant method for finding roots of a function.
Este método implementa el método de la secante para encontrar raíces de una función.
"""

def secante(funcion, x0, x1, tolerancia):
    iteraciones = 0
    error = 1
    while (error > tolerancia):
        iteraciones += 1
        x2 = x1 - (funcion(x1) * (x0-x1))/(funcion(x0) - funcion(x1))
        error = abs(x2 - x1)
        x0 = x1
        x1 = x2
    
    return x2, iteraciones