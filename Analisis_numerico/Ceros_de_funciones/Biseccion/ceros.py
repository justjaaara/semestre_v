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