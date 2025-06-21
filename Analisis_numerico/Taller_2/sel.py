import numpy as np
import time

def gauss_seidel_matrices(A, b, x0, tol):
    """
    Implementación del método de Gauss Seidel.
    -----------
    Parámetros
    -----------
    - A: matriz de coeficientes cuadrada
    - b: vector de términos independientes
    - x0: vector inicial --> Si no me da el dato se asume que el vector es el vector nulo
    - tol: Exactitud con la cual encontraremos la solución del sistema de ecuaciones lineales (SEL). Si no me dan este dato se asume que la tolerancia es 1e-6
    -----------
    Nota
    ------------
    - TANTO LA MATRIZ A COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
    - AMBAS TIENE QUE TENER DIAGONAL ESTRICTAMENTE DOMINANTE
    -------------
    Retorna:
        x0: solución final
        error_final: error de la última iteración
        errores: lista de errores por iteración
        iteraciones: lista de número de iteración (1, 2, ...)
        time_total: tiempo total de ejecución
    """
    D = np.diag(np.diag(A)) # Obtenemos la matriz diagonal
    L = D - np.tril(A) # Obtenemos la matriz inferior
    U = D - np.triu(A) # Obtenemos la matriz superior
    Tg = np.dot(np.linalg.inv(D-L), U)
    Cg = np.dot(np.linalg.inv(D-L), b)
    v_propios, vect_propios = np.linalg.eig(Tg)
    radio = max(abs(v_propios))
    print(f"Radio espectral: {radio}")
    if radio<1:
        import time
        time_start = time.time()
        error = 1
        iteracion = 1
        errores = []
        while (error > tol):
            x1 = np.dot(Tg,x0) + Cg
            error = np.max(np.abs(x1-x0))
            errores.append(error)
            x0 = np.copy(x1)
            iteracion += 1
        time_end = time.time()
        time_total = time_end - time_start
        return x0, error, errores, time_total, iteracion-1
            
    else:
        print("El sistema iterativo no converge con el método de Jacobi")
        return None, None, [], 0, 0

import numpy as np

def gauss_seidel_sumas(A, b, x0=None, tol=1e-10, max_iter=100):
    """
    Método de Gauss-Seidel para resolver Ax = b con suma de cambios por iteración.
    
    Parámetros:
        A : array-like (n x n)
        b : array-like (n)
        x0 : array-like (n), condiciones iniciales (opcional)
        tol : tolerancia para el criterio de parada
        max_iter : número máximo de iteraciones
    
    Retorna:
        x : solución aproximada (array de NumPy)
        error_final : error de la última iteración
        errores : lista con el error por iteración (norma infinito)
        iteraciones : lista de número de iteración (1, 2, ...)
        tiempo_total : tiempo de ejecución
    """
    import time
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    if x0 is None:
        x = np.zeros_like(b, dtype=float)
    else:
        x = np.array(x0, dtype=float)

    suma_iteraciones = []
    errores = []

    time_start = time.time()

    for it in range(1, max_iter+1):
        x_new = x.copy()
        suma_cambios = 0.0

        for i in range(n):
            suma = np.dot(A[i, :i], x_new[:i]) + np.dot(A[i, i+1:], x[i+1:])
            nuevo_valor = (b[i] - suma) / A[i, i]
            suma_cambios += abs(nuevo_valor - x[i])
            x_new[i] = nuevo_valor

        suma_iteraciones.append(suma_cambios)
        error = np.max(np.abs(x_new - x))
        errores.append(error)

        if suma_cambios < tol:
            break

        x = x_new

    time_end = time.time()
    tiempo_total = time_end - time_start
    error_final = errores[-1] if errores else None
    iteraciones = it

    return x, error_final, errores, tiempo_total, iteraciones


def jacobi_con_matrices(A,b,x0,tol):
    """
    Implementación del método de Jacobi utilizando matrices.
    -----------
    Parámetros
    -----------
    - A: matriz de coeficientes cuadrada
    - b: vector de términos independientes
    - x0: vector inicial --> Si no me da el dato se asume que el vector es el vector nulo
    - tol: Exactitud con la cual encontraremos la solución del sistema de ecuaciones lineales (SEL). Si no me dan este dato se asume que la tolerancia es 1e-6
    -----------
    Nota
    ------------
    - TANTO LA MATRIZ A COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
    - AMBAS TIENE QUE TENER DIAGONAL ESTRICTAMENTE DOMINANTE
    """
    D = np.diag(np.diag(A)) # Obtenemos la matriz diagonal
    L = D - np.tril(A) # Obtenemos la matriz inferior
    U = D - np.triu(A) # Obtenemos la matriz superior
    Tj = np.dot(np.linalg.inv(D), L+U)
    Cj = np.dot(np.linalg.inv(D), b)
    v_propios, vect_propios = np.linalg.eig(Tj)
    radio = max(abs(v_propios))
    print(radio)
    if radio<1:
        time_start = time.time()
        error = 1
        iteracion = 1
        errores = []
        while (error > tol):
            x1 = np.dot(Tj,x0) + Cj
            error = np.max(np.abs(x1-x0))
            errores.append(error)
            x0 = np.copy(x1)
            # print(f"Iteración {iteracion}: {x1}, Error: {error}")
            iteracion += 1
        time_end = time.time()
        time_total = time_end - time_start
        return x0, error, errores, time_total, iteracion
            
    else:
        print("El sistema iterativo no converge con el método de Jacobi")

def jacobi_con_sumas(A, b, x0, n_max, tol):
    """
    -----------
    Parametros
    -----------
    - A: matriz de coeficientes cuadrada
    - b: vector de términos independientes
    - x0: vector inicial --> Si no me da el dato se asume que el vector es el vector nulo
    - n_max: número máximo de iteraciones
    - tol: Exactitud con la cual encontraremos la solución del sistema de ecuaciones lineales (SEL). Si no me dan este dato se asume que la tolerancia es 1e-6
    -----------
    Nota
    ------------
    - TANTO LA MATRIZ A COMO EL VECTOR b Y X0 TIENEN QUE SER DE TIPO FLOTANTE
    - AMBAS TIENE QUE TENER DIAGONAL ESTRICTAMENTE DOMINANTE
    """

    n = len(b)  # -> Tamaño del vector b que es el mismo de A porque es cuadrada
    x1 = np.zeros(n)
    error = 10
    iteracion = 0
    errores = []
    
    
    time_start = time.time()
    while error > tol and iteracion < n_max:
        for i in range(n):
            suma = 0  # Inicializar suma para cada fila
            for j in range(n):
                if i != j:
                    suma += np.dot(A[i][j], x0[j])  # Acumular la suma correctamente
            x1[i] = (b[i] - suma) / A[i][i]
        
        # Calculo el error como la norma infinito de la diferencia
        error = np.max(np.abs(x1 - x0))
        errores.append(error)
        
        # Actualizo el vector inicial
        x0 = np.copy(x1)
        iteracion += 1
        
        # print(f"Iteración {iteracion}: {x1}, Error: {error}")
    time_end = time.time()
    tiempo_total = time_end - time_start
    
    return x1, error, errores, tiempo_total, iteracion