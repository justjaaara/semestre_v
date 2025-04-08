"""
El volumen V del líquido contenido en un tanque esférico de radio r está relacionado con la profundidad h del líquido por
V=(πh²(3r-h))/3

Determine h para r=1m y V=0.75m³

Solución usando el método de Bisección con tol=10-6
Solución usando el método de Falsa posición con tol=10-6
Solución usando el método de Newton con tol=10-6



Los tres de manera computacional, adicional el tercero a mano con todo detalle de las iteraciones. 

Den organizar para que en cada ejercicio imprima la tabla con información de los datos .

Deben adjuntar un archivo en extensión ipynb, no URL.
"""
import sys
sys.path.append('Ceros_de_funciones')
import numpy as np
import sympy as sp

r = 1
V = 0.75

def Biseccion(funcion,a,b,tolerancia):
    
    if funcion(a) * funcion(b) > 0:
        print('La función no cumple el teorema en el intervalo inicial')
        return
    else:
        print('Buscando.....')
        iteracion = 0
        while (abs(b-a) > tolerancia):
            iteracion+=1
            p = (a+b)/2
            if (funcion(a)*funcion(p)) > 0:
                a = p
            else:
                b = p
        return iteracion,p

def falsa_posicion(funcion,a,b,tolerancia):
    
    if funcion(a) * funcion(b) > 0:
        print('La función no cumple el teorema en el intervalo inicial')
        return
    else:
        print('Buscando.....')
        iteracion = 0
        p = b-funcion(b)*(a-b)/(funcion(a)-funcion(b))
        while (abs(funcion(p))>tolerancia):
            iteracion+=1
            p = b-funcion(b)*(a-b)/(funcion(a)-funcion(b))
            if (funcion(a)*funcion(p)) > 0:
                a = p
            else:
                b = p
        return iteracion,p

def newton_rapshon(funcion,x0,tolerancia,x):
    derivada_funcion = sp.diff(funcion,x)
    print(derivada_funcion)
    x1 : float = x0 - (funcion.evalf(subs={x:x0})/derivada_funcion.evalf(subs={x: x0}))
    iteraciones = 0
    while abs(x1 - x0) > tolerancia:
        iteraciones += 1
        x0 = x1
        x1 = x0 - (funcion.evalf(subs={x: x0}) / derivada_funcion.evalf(subs={x: x0}))
    return iteraciones, x1

def secante(funcion, x0, x1, tolerancia):
    iteraciones = 0
    error = 1
    while (error > tolerancia):
        iteraciones += 1
        x2 = x1 - (funcion(x1) * (x0-x1))/(funcion(x0) - funcion(x1))
        error = abs(x2 - x1)
        x0 = x1
        x1 = x2
    
    return iteraciones, x2

funcion = lambda h: (np.pi*(h**2) * ((3*r)-h))/3 - V
x = sp.symbols('x')
funcion_simbolica = (sp.pi*(x**2) * ((3*r)-x))/3 - V


iteraciones_biseccion, resultado_biseccion = Biseccion(funcion, 0, 1, 1e-6)
iteraciones_falsa_posicion, resultado_falsa_posicion = falsa_posicion(funcion, 0, 1, 1e-6)
iteraciones_newton, resultado_newton = newton_rapshon(funcion_simbolica, 0.5, 1e-6, x)  
iteraciones_secante, resultado_secante = secante(funcion, 1, 2, 1e-6)




print(f"Resultados de Bisección: {resultado_biseccion}")
print(f"Número de iteraciones Bisección: {iteraciones_biseccion}")
print("-------------------------------------------------------")
print(f"Resultados de Falsa Posición: {resultado_falsa_posicion}")
print(f"Número de iteraciones Falsa Posición: {iteraciones_falsa_posicion}")
print("-------------------------------------------------------")
print(f"Resultados de Newton: {resultado_newton}")
print(f"Número de iteraciones Newton: {iteraciones_newton}")
print("-------------------------------------------------------")
print(f"Resultados de Secante: {resultado_secante}")
print(f"Número de iteraciones Secante: {iteraciones_secante}")
print("-------------------------------------------------------")
