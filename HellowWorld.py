nombre = 'Angel'

def seleccionDatos(nombre):
    print(nombre[1:5])

def condicionalIf():
    edad = int(input('Dame edad '))
    if edad > 5:
        print ('mayor')
    else: 
        print ('menor')

def entradaDatos():
    entrada = input ('Dame tu nombre ')

def cicloWhile():
    x = 10
    while x != 0:
        print (f'valor de x: {x} ')
        x -= 1

def cicloFor():
    for z in range(1,10):
        print(z)

def cicloForEach():
    numeros = [1,2,3,4,5,6,8,9]
    for i in numeros :
        print (i)


def tablaMult():
    numero = int(input ('Dame un numero: '))
    for z in range(1,11):
        print(f'{z} x {numero} = { z * numero }')

#tablaMult()


def lista():
    #peticion = int ( input ('Dame tu numero de la suerte'));

    numeros = [1...]
    deportes = ['fut','bask','voley','beis','tennis']
    deportes.reverse()
    deportes.append('adios')
    deportes.reverse()
    deportes.extend(numeros) 
    print( numeros )
    

lista()