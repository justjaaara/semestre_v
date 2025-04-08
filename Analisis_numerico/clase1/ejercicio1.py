'''
Rea;ozar un programa que me reciba por teclado un numero e imprima cada dígito de este número y 
adicional imprima la suma de los digitos, sin utilizar ninguna de las rutinas disponibles en numpy
'''

input_number = input('Ingrese un número cualpuiera: ')

suma_digitos = 0
for number in input_number:
    if (int(number) % 2 == 0) and (int(number) % 3 == 0):
        print(number)
    suma_digitos += int(number)

print(f'La suma de los dígitos es {suma_digitos}')


