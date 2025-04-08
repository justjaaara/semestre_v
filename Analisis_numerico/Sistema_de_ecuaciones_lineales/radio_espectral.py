import sys 
sys.path.append('/Sistema_de_ecuaciones_lineales')
import numpy as np

#Declarando la matrizo

B = np.array([[ -1,  2,  0],
              [  2, -3,  1],
              [  0,  1,  2]])

l, v= np.linalg.eig(B)
#l son las soluciones del polinomio lamda 1, lambda 2, lambda 3
print(l)

#Radio espectral es el max(abs(l))
radio_espectral = max(abs(l))
print(radio_espectral)