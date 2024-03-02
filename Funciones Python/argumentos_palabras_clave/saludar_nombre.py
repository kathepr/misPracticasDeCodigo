#Si desconozco el orden en el que debo enviar los argumentos

#Puedo usar ARGUMENTOS CON PALABRAS CLAVE:
#Permiten pasar valores a una funcion, identificandolos explicitamente por el nombre
#del parametro.

def saludar (nombre, saludo):
    mensaje = f"¡{saludo}, {nombre}!"
    print (mensaje)


saludar (saludo="Hola", nombre="Ana") #Estos son los argumentos con palabras clave
                                      #aunque no coloque en orden los parametros
                                      #Los argumentos con palabras claves, me van a ayudar con la posición.
         
