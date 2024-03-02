def sum_numeros (*numeros): #Puedo crear un parametro que reciba muchos números
                            # o muchas variables.
    print(numeros)
    resultado = sum(numeros)
    print(resultado)


sum_numeros(1, 2, 3, 4, 5, 6) #puedo enviar la cantidad de argumentos que quiero enviarle a mi función

#Dentro de los argumentos arbitrarios, tenemos dos tipos:
#1. Argumentos posicionales arbitrarios *args
#      Hace referencia a los argumentos que queremos enviar
#      El asterisco lo tenemos que conocar antes del nombre del parametro que vamos a recibir
#      En este caso *numeros
#Con esto, le estamos diciendo a Python que acepte cualquier tipo de argumento posicional
#y los empaquete en una tupla. 



#2. Argumentos de palabra clave arbitrarios **kwargs
#Mira el archivo Python que se llama
# argumentos_palabra_clave_arbitrarios