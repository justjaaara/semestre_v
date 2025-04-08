import numpy as np
import sympy as sp

def Biseccion(funcion, a, b, tolerancia):
    if funcion(a) * funcion(b) >= 0:
        print('La función no cumple el teorema en el intervalo inicial')
        return None
    iteracion = 0
    while (abs(b-a) > tolerancia):
        iteracion += 1
        p = (a + b) / 2
        if funcion(p) == 0:
            return iteracion, p
        elif funcion(a) * funcion(p) > 0:
            a = p
        else:
            b = p
    return iteracion, p

# Definir variables simbólicas
A, t = sp.symbols('A t')
C_t = A * t * sp.exp(-t / 3)

# Derivar y encontrar el máximo
derivada = sp.diff(C_t, t)
derivada_sustituida_A = derivada.subs(A, 1)
derivada_evaluada = sp.lambdify(t, derivada_sustituida_A, 'numpy')

# Encontrar el tiempo de concentración máxima
tiempo_max = Biseccion(derivada_evaluada, 0.1, 10, 1e-6)  # Asegurando un intervalo válido
t_max = tiempo_max[1]

# Calcular A usando la ecuación C(t) = 1 mg/ml
A_valor = 1 / (t_max * np.exp(-t_max / 3))

print(f"Para alcanzar la máxima concentración segura de 1 mg/ml, se debe inyectar {A_valor:.4f} unidades y se presenta a las {t_max:.4f} horas\n")

# Encontrar el tiempo cuando C(t) = 0.25 mg/ml
funcion_b = lambda t: A_valor * t * np.exp(-t / 3) - 0.25
tiempo_b = Biseccion(funcion_b, t_max, 20, 1e-6)
t_b = tiempo_b[1]

print(f"La segunda inyección se debe aplicar a los {t_b * 60:.0f} minutos\n")

# Calcular el tiempo de la tercera inyección
dosis_2 = 0.75 * A_valor
funcion_c = lambda t: (A_valor * t * np.exp(-t / 3)) + (dosis_2 * (t - t_b) * np.exp(-(t - t_b) / 3)) - 0.25

tiempo_c = Biseccion(funcion_c, t_b + 0.1, 20, 1e-6)
t_c = tiempo_c[1]

print(f"La tercera inyección se debe aplicar a las {t_c:.4f} horas")
