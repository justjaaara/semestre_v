import sympy as sp

def newton_rapshon(funcion,x0,tolerancia,x):
    derivada_funcion = sp.diff(funcion,x)
    x1 : float = x0 - (funcion.evalf(subs={x:x0})/derivada_funcion.evalf(subs={x: x0}))
    iteraciones = 0
    while abs(x1 - x0) > tolerancia:
        iteraciones += 1
        x0 = x1
        x1 = x0 - (funcion.evalf(subs={x: x0}) / derivada_funcion.evalf(subs={x: x0}))
    return x1, iteraciones

# x = sp.symbols('x')
# f = x**2 - 6
# x0 = 1  # -> Valor inicial arbitrario > 0
# tolerancia = 1e-4

# x, iteraciones = newton_rapshon(f, x0, tolerancia)
# print(f"La raíz es: {x}")
# print(f"El número de iteraciones es: {iteraciones}")

