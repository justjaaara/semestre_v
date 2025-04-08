import sympy as sp
import numpy as np

h = 0.1
x0 = 1.2
L = 0.05
R = 2
i_t = {
    1.0: 8.2277,
    1.1: 7.2428,
    1.2: 5.9908,
    1.3: 4.5260,
    1.4: 2.9122
}
#Calculando la derivada centrada
i_aproximada = (i_t[round(x0+h,2)] - i_t[round(x0-h,2)])/(2*h)

#Hallando la derivada de la función para comparar 
x = sp.symbols('x')
funcion = 10*sp.exp(-x/10)*sp.sin(2*x)
derivada_funcion = sp.diff(funcion,x)

i_derivada_analitica = derivada_funcion.evalf(subs={x:x0}) # Funcion analitica derivada y evaluda en 1.2 

error_absoluto = abs(i_derivada_analitica - i_aproximada)

E = (L * i_derivada_analitica) + (R * i_t[x0] ) # -> Voltaje con los valores hallados anteriormente

# Imprimiendo los valores
print(i_aproximada)
print(i_derivada_analitica)
print(error_absoluto)
print(E)

