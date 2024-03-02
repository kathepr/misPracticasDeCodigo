# Los valores de la función se les conoce como argumentos

# Los parametros son variables usadas por las funciones para recibir
# información necesaria para realizar una tarea especifica. 

def saludar(nombre): #nombre sería el parametro, ahí voy a recibir un valor en especifico
    mensaje = f"\n¡Hola, {nombre}!, ¡Bienvenido al curso de funciones!\n"
    print (mensaje)


saludar("Juan") #Aquí llame a la función por su nombre
                #Cuando hacemos el llamado a la función y le enviamos informacion
                # se le conoce como argumento. "Juan" es el argumento. 
