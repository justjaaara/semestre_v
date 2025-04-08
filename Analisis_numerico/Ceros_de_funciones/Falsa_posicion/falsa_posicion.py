def falsa_posicion(funcion,a,b,tolerancia):
    
    if funcion(a) * funcion(b) > 0:
        print('La función no cumple el teorema en el intervalo inicial')
        return
    else:
        print('Buscando.....')
        iteracion = 0
        p = b-funcion(b)*(a-b)/(funcion(a)-funcion(b))
        while (abs(funcion(p))>tolerancia):
            iteracion+=1
            p = b-funcion(b)*(a-b)/(funcion(a)-funcion(b))
            if (funcion(a)*funcion(p)) > 0:
                a = p
            else:
                b = p
        return iteracion,p