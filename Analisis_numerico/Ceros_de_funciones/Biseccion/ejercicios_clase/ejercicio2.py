import numpy as np
import matplotlib.pyplot as plt

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

funcion = lambda x: (x+np.sqrt(x))*(20-x+np.sqrt(20-x))-155.55
x= np.linspace(0,20,100)
plt.axhline(0, color='red', linewidth=1, linestyle='dashed')
plt.plot(x, funcion(x), 'b')
plt.ylim(-25,25)

# Hallando X en el intervalo [5,7.5]
iteraciones_x, x = Biseccion(funcion,5,7.5,1e-4)
print(f"El valor de X: {x} en {iteraciones_x} iteraciones.")

# Hallando Y en el intervalo [12.5,17.5]
iteraciones_y, y = Biseccion(funcion,12.5,17.5,1e-4)
print(f"El valor de Y: {y} en {iteraciones_y} iteraciones.")

# comprobando
print(f"Comprobando que los valores son correctos la suma debe ser 20 \n x+y={x+y}")

# Show plot at the end
plt.show()