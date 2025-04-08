import sys
sys.path.append('Ceros_de_funciones')

from Biseccion.ceros import Biseccion
from Newton_Rapshon.newton import newton_rapshon
from Falsa_posicion.falsa_posicion import falsa_posicion
import sympy as sp
import numpy as np

#TODO: Agregar la imagen del problema

# Variables de la función
L = 10
r = 1
V = 10
tolerancia = 1e-2

# Calculando con newton Rapshon
h = sp.symbols('h')
funcion = L*((1/2)*np.pi - sp.asin(h) - h*(r**2-h**2)**(1/2)) - V

resultado_newton, iteraciones_newton = newton_rapshon(funcion, 0.5, tolerancia, h)

#Funcion para bisección y falsa posición
f = lambda x: L*((1/2)*np.pi - np.arcsin(x) - x*(r**2-x**2)**(1/2)) - V

#Calculando para biseccion
iteraciones_biseccion, resultado_biseccion = Biseccion(f, 0, 1, tolerancia)

#Calculando para falsa posición
iteraciones_falsa_posicion, resultado_falsa_posicion = falsa_posicion(f, 0, 1, tolerancia)

print(f"Resultado en newton {resultado_newton} con {iteraciones_newton} iteraciones")
print(f"Resultado en biseccion {resultado_biseccion} con {iteraciones_biseccion} iteraciones")
print(f"Resultado en falsa_posicion {resultado_falsa_posicion} con {iteraciones_falsa_posicion} iteraciones")

# Calculando la profundidad por medio de los metodos se calculó el h pero se neceita hacer r-h para obtener la profundidad en ese momento

profundidad = r - resultado_newton
print(f"La profundidad es {profundidad}")



