import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#DEclarar x como variable simbólica

x = sp.symbols('x')
#función
f=2**x
#Derivada
df=sp.diff(f,x)

x0 = 0
#El polinomio
P = (f.evalf(subs={x:x0}) + df.evalf(subs={x:x0})*(x-x0))

# Gráfica del polinomio versus la función
delta = 2
u_x = np.linspace(x0-delta, x0+delta,100)
P = sp.lambdify(x,P)
f = sp.lambdify(x,f)
plt.plot(u_x,f(u_x), 'b', label='$2^x$')
plt.plot(u_x,P(u_x), 'r', label='$P(x)$')
plt.legend()
plt.xlabel('Eje x')
plt.ylabel('Eje y')