def funcion ():
    x = 10   # x es de ambito local
    print (x)

#Cuando trabajamos con variables que están dentro de la función
#Estas tienen ambitos.
#Las variables definidas dentro de una función se consideran de AMBITO LOCAL
#Solo se puede acceder a ella dentro de la función y no por fuera


funcion()

# print (x)  ----> Si yo hago esto, es decir, 

#Si yo intento imprimir en pantalla el valor que está dentro de la funcion
#ME VA A MARCAR UN ERROR, porque no la he creado fuera de la función