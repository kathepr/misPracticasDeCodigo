#Alternativa de uso # 1: Las variables se declaran previamente

nombre = "Carla"
edad = 25

print("¡Hola! {} tiene {} años".format(nombre,edad))



# Alternativa # 2: Los valores de las variables se incluyen dentro del método format.

print("¡Hola! {nombre} tiene {edad} años".format(nombre = "Veronica",edad = 29))



#Alternativa # 3: Dentro de los corchetes, colocamos la posición de las variables. 
#De esa manera, podemos colocar cual queremos primero y cual después.

print("¡Hola! {0} tiene {1} años".format(nombre,edad))
print("¡Hola! {1} tiene {0} años".format(nombre,edad))