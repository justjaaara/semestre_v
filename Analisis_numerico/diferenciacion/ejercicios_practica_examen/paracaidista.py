import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

m = 68.1
c= 15 # -> Constante resistencia del aire`
g=9.8
v = [0]
v_analitica = [0]
h= 0.1

t0 = 0
tf =  120 

while (t0 < tf):
    v.append(h*(g-((c/m)*v[-1]))+v[-1])
    v_analitica.append(((g*m)/c)*(1-np.exp(-(c/m)*t0)))
    t0 += h

#Calculando el error entre la velocidad numerica y analitica
error_absoluto = abs(v_analitica[-1] - v[-1])
print(f"EL erorr absoluto es {error_absoluto}")

#Graficando la velocidad analítica y velocidad numérica
plt.plot(v)
plt.plot(v_analitica)
plt.show()
