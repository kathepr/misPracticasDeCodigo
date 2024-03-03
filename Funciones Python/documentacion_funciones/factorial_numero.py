#Documentación de la función

#Raises: Indica las excepciones que puede generar una función
#        Puede proporcionar información sobre como manejarlas
#        Se especifica el error que puede generar


def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Parametros:
    n (int) número entero no negativo

    Returns:
    resultado_factorial (int) El factorial de n

    Raises RecursionError: Si n es un número negativo. 
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    

resultado_factorial=factorial(5)
print(resultado_factorial)




#                      ¿COMO CONSULTO LA DOCUMENTACIÓN DE LA FUNCIÓN?

#Alternativa #1:
help(factorial) #NOS PERMITE CONSULTAR LA DOCUMENTACIÓN DE LA FUNCIÓN
                #Entre parentesis se coloca el nombre de la funcion


#Alternativa #2:
# print(factorial.__doc__) #NOS PERMITE CONSULTAR LA DOCUMENTACIÓN DE LA FUNCIÓN

