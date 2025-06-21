import numpy as np

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