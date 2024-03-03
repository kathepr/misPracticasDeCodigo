def cuadrado(x):
    return x**2


def cubo(x):
    return x**3

def aplicar_funcion_a_lista(funcion, lista): #Esta es la FUNCION DE ORDEN SUPERIOR
                                            # Se va a encargar de recibir la funcion como argumento 
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


lista_numeros = [1, 2, 3, 4, 5]
resultado = aplicar_funcion_a_lista(cuadrado, lista_numeros)
print(resultado)        