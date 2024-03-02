#Cuando queremos que nos retornen los valores de la funcion
#Debemos usar return: Le permite a una funcion devolver un resultado en el punto de llamada 

def suma(a, b):
    resultado = a + b
    return resultado #Se coloca return y el nombre de la variable que se quiere retornar. 
    
#Opcion 1: Crear una variable para retornar el resultado
resultado_suma = suma(3,5)
print(resultado_suma) 

#Opcion 2: Usar directamente la llamada de la funcion para retornar resultado
print(suma(5,5))