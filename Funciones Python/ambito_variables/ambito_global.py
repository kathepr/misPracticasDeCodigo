# Una variable definida/declarada fuera de cualquier función o bloque
# se considera de AMBITO GLOBAL.

#Puede ser accedida y modificada desde cualquier parte del código
#Incluso dentro o fuera de las funciones

y = 20


def funcion():
    print(y, "impresión dentro de la función")


funcion()
print(y, "impresión fuera de la función\n")



# ¿Que sucede si quiero modificar el valor de la variable 'Y'/'X' dentro de la función?

# Solo me va a permitir cambiar la variable dentro de la función y no por fuera
#Como se muestra en el siguiente ejemplo.
#La variable global, sigue con el mismo valor. Y la variable local, fue la única que se modificó


x= 20 #variable de ambito global

def funcion2():
    x=30 #variable de ambito local, esta no puede modificar la global
    print(x, "impresión dentro de la función")


funcion2()
print(x, "impresión fuera de la función")
