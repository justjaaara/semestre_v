import numpy as np

def minimos_cuadrados(x, y):
    """
    Ajuste de mínimos cuadrados para una función lineal.
    
    Parameters:
    x (array-like): Valores de la variable independiente.
    y (array-like): Valores de la variable dependiente.
    
    Returns:
    tuple: Coeficientes del polinomio ajustado (a0, a1).
    """
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sx2 = np.sum(x**2)
    Sxy = np.sum(x*y)
    n = len(x) # numero de datoso

    a0 = ((Sy * Sx2) - (Sx * Sxy)) / ((n * Sx2) - (Sx)**2)
    a1 = ((n * Sxy) - (Sx * Sy)) / ((n * Sx2) - (Sx)**2)

    return a0, a1
