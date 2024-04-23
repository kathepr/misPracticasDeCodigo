print ("Sistema para calcular el promedio de un alumno")
nombre = input ("¡Hola! ¿Cual es tu nombre? ")
math = float(input(nombre + " ¿Cual es tu calificacion en matematicas? "))
quim = float(input(nombre + " ¿Cual es tu calificación en química? "))
bio = float(input(nombre + " ¿Cual es tu calificación en biología? "))

promedio = (math + quim + bio)/3

if promedio>=6:
    print (nombre," ¡Felicitaciones! Has aprobado con un promedio de: ", promedio)


print ("Fin.")




