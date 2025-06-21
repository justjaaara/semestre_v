import numpy as np

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

def runge_kutta(f,a,b,h,y0):
    n = int((b-a)/h)
    wrk=[y0]
    for i in range(n):
        k1= h*f(a+i*h, wrk[i])
        k2= h*f(a+i*h+0.5*h, wrk[i]+0.5*k1)
        k3= h*f(a+i*h+0.5*h, wrk[i]+0.5*k2)
        k4= h*f(a+(i+1)*h, wrk[i]+k3)
        wrk.append(wrk[i]+(1/6)*(k1+2*k2+2*k3+k4))
    return np.linspace(a,b,n+1),wrk