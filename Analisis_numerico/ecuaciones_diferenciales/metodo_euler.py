
import numpy as np
def metodo_euler(funcion, intervalo_a, intervalo_b, condiciones_iniciales, h):
    """
    Este método calcula la aproximación de la ecuación diferencial por el método de Euler

    Parameters
    ----------
    - funcion: Ecuación diferencial a aproximar
    - intervalo_a: Valor del intervalo en a
    - intervalo_b: Valor del intervalo en b
    - h: Esparcimiento
    - condiciones_iniciales: Condiciones iniciales de la ecuación diferencial

    Returns
    -------

    """

    #Calculando n
    n = (intervalo_b - intervalo_a) / h
    n = int(n)
    #Discretizando
    tiempos = []
    for i in range(n+1):
        t_i = intervalo_a + (i*h)
        tiempos.append(t_i)
    
    #Aproximando euler
    w_eu = np.copy(condiciones_iniciales)
    for i in range(n):
        y_siguiente = w_eu[i] + h * funcion(tiempos[i], w_eu[i])
        w_eu = np.append(w_eu, y_siguiente)
    
    return tiempos, w_eu


def metodo_euler_profe(f,a,b,h,y0):
    """
    Parameters
    ----------
    f : function
        Ecuación diferencial a aproximar.
    a : float
        Valor del intervalo en a.
    b : float
        Valor del intervalo en b.
    h : float
        Esparcimiento.
    y0 : list
        Condiciones iniciales de la ecuación diferencial.
    Returns
    -------
    tiempos : numpy.ndarray
        Arreglo de tiempos discretizados.
    weu : list
        Aproximación de la ecuación diferencial por el método de Euler.
    """
    weu = [y0]
    n = int((b-a)/h)
    for i in range(n):
        weu.append(weu[i] + h*f(a + i*h,weu[i]))
    return np.linspace(a,b,n+1),weu

    


#testeando

# y_p = lambda t,y: 1 + (y/t)
# a = 1
# b = 2
# y0 = [2]
# h = 0.5

# tiempos, y_i = metodo_euler(y_p, a, b, y0, h)
# print("tiempos: ", tiempos)
# print("y_i: ", y_i)

# #Ejemplo de la profe
# aprox = metodo_euler_profe(y_p, a, b, h, y0[0])
# print("Aproximacion: ", aprox)
