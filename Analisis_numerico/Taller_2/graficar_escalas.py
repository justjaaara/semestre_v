import numpy as np
import matplotlib.pyplot as plt


def graficar_escalas(x_d, y_d):
    """
    Función que grafica los datos en escalas diferentes escalas.

    Parámetros
    ----------
    x_d : array
        Datos en el eje x.
    y_d : array
        Datos en el eje y.
    Returns
    -------
    graficas : list
        Lista de graficas generadas.
        
    """
    plt.figure(figsize=(12, 12), dpi=100)
    plt.subplot(331)
    plt.plot(x_d , y_d, 'or', label='Datos observados') # graficos de dispersión
    plt.subplot(332)
    plt.plot(x_d, np.sqrt(y_d), 'ob')
    plt.xlabel('x')
    plt.ylabel('$\sqrt{y}$')
    plt.subplot(333)
    plt.plot(x_d, 1/y_d, 'ob')
    plt.xlabel('x')
    plt.ylabel('$1/y$')
    plt.subplot(334)
    plt.plot(x_d**2, y_d, 'ob')
    plt.xlabel('$x^2$')
    plt.ylabel('y')
    plt.subplot(335)
    plt.plot(x_d**3, y_d, 'ob')
    plt.xlabel('$x^3$')
    plt.ylabel('y')
    plt.subplot(336)
    plt.plot(np.log(x_d), y_d, 'ob')
    plt.xlabel('$\log(x)$')
    plt.ylabel('y')
    plt.subplot(337)
    plt.plot(x_d, np.log(y_d), 'ob')
    plt.ylabel('$\log(y)$')
    plt.xlabel('x')
    plt.subplot(338)
    plt.plot(np.sqrt(x_d), y_d, 'ob')
    plt.xlabel('$\sqrt{x}$')
    plt.ylabel('y')
    plt.subplot(339)
    plt.plot(np.log(x_d), np.log(y_d), 'ob')
    plt.xlabel('$\log(x)$')
    plt.ylabel('$\log(y)$')
    plt.subplots_adjust(wspace=0.4, hspace=0.6)  # Ajusta el espacio entre subgráficos
    return plt