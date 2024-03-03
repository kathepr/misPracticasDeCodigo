# FUNCIONES DE ORDEN SUPERIOR:
# Funciones que pueden tomar una o más funciones con argumentos
# Y devolver funciones como resultado

def cuadrado(x):
    return x**2


def cubo(x):
    return x**3

def aplicar(funcion, valor): #Esta es la FUNCION DE ORDEN SUPERIOR
                             # Se va a encargar de recibir la funcion como argumento y el valor al que le vamos a 
                             # aplicar la potencia al cuadrado o al cubo
    return funcion(valor)


resultado = aplicar(cuadrado,5) #Aquí pongo entre parentesis el nombre de la función que quiero aplica
print(resultado)                # Y despues de una coma, el valor
