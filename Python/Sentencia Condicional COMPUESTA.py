print ("Sistema para calcular el promedio de un alumno")
nombre = input("¡Hola! ¿Cuál es tu nombre? ")
math = float (input(nombre + " ¿Cuál es tu calificación en matemáticas? "))
quim = float (input(nombre + " ¿Cuál es tu calificación en química? "))
bio = float (input (nombre + " ¿Cuál es tu calificación en biología? "))

promedio = (math + quim + bio)/3

if promedio>=6:
    print ("¡Felicidades " + nombre + "! Has aprobado con un promedio de: ", promedio)
    print ("Si redondeamos tu promedio, nos da un resultado de: ", round(promedio,2))
else:
    print ("Lo lamento " + nombre + ". Has reprobado con un promedio de: ", promedio)  
    print ("Si redondeamos tu promedio, nos da un resultado de: ", round (promedio,2) ) #round nos ayuda a controlar la cantidad de decimales a mostrar
                                                                                        #Lo primero que se pone es el #flotante, despues sigue la cantidad de decimales que deseas mostrar
print ("Fin.")