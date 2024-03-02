# La mayoría de los objetos se pasan por referencia objeto
# Esto significa que se pasa una referencia del objeto original a la función

#Cualquier modificación realizada dentro de la función, afectará al objeto original, fuera de la funcion

#Estos objetos pueden ser listas, diccionarios y objetos personalizados

def modificar_lista(lista):
    lista.append(4) #append es para añadir un valor, en este caso el #4
    print ("Dentro de la función: ", lista) 


mi_lista=[1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función: ", mi_lista) #Aquí se pasa por referencia un objeto

#Paso por referencia a objeto, si modifica el objeto original
#Los tipos de datos que se pasan por referencia pueden ser listas, diccionarios y objetos personalizados