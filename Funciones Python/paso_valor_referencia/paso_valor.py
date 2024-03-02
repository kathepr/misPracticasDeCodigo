def modificar_valor(x):
    x = x + 10
    print("Dentro de la función: ", x) #Si se modifica el valor
    


numero = 5
modificar_valor(numero)
print("Fuera de la funcion: ", numero) # No se modifica el valor

#En paso por valor, no se modifican los valores
# Los tipos de datos pueden ser: enteros, flotantes y cadenas