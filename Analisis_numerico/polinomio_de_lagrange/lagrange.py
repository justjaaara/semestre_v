import sympy as sp
import numpy as np

def lagrange_pol(x_data, y_data):
    x = sp.symbols('x')
    
    P = 0 # Acumulador del polinomio
    n = len(x_data) # Número de datos
    
    for i in range(n):
        Li = 1
        for j in range(n):
            if j != i:
                Li *= (x - x_data[j]) / (x_data[i] - x_data[j])
        P += Li * y_data[i]
    return sp.expand(P)