#Documentación de funciones:
#Comunica a otros desarrolladores el proposito y uso de una función
#También lo ubica a uno mismo, despues de muchos años, cuando quiera volver a la función

#La documentacion de funciones se hace con comillas triples
#Se colocan despues de la definición de una función

def operaciones_basicas(a, b): 
    """
    Realiza operaciones básicas entre dos números.

    Parametros:
    a (int o float), es el primer número
    b (int o float), es el segundo número

    Returns:
            Una tupla con los resultados de las operaciones.
            -suma (int o float): Suma de a y b
            -resta (int o float): Resta de a y b
            -multiplicación (int o float): Producto de a y b
            -división (float): a divido por b (si b no es cero)
    """
    
    suma = a + b
    resta= a - b
    multiplicacion = a * b
    division = a/b
    return suma, resta, division, multiplicacion 


resultados=operaciones_basicas(2, 2)
print(resultados) 




#                      ¿COMO CONSULTO LA DOCUMENTACIÓN DE LA FUNCIÓN?

#Alternativa #1:
# help(operaciones_basicas) #NOS PERMITE CONSULTAR LA DOCUMENTACIÓN DE LA FUNCIÓN
                            #Entre parentesis se coloca el nombre de la funcion


#Alternativa #2:
print(operaciones_basicas.__doc__) #NOS PERMITE CONSULTAR LA DOCUMENTACIÓN DE LA FUNCIÓN

