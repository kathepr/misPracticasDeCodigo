# ¿Que sucede si quiero modificar el valor de la variable 'Y'/'X' dentro de la función?

# Solo me va a permitir cambiar la variable dentro de la función y no por fuera
#Como se muestra en el siguiente ejemplo.
#La variable global, sigue con el mismo valor. Y la variable local, fue la única que se modificó

                      #OJO: IMPORTANTE

# PEROOOO, si utilizo la plabra reservada global
#Le indico a Python que quiero modificar el valor de la variable global


x= 20 

def funcion2():
    global x #hay que colocar antes del nombre de la variable la palabra global
    x = 30   #Posteriormente se le añade el nuevo valor.

    print(x, "impresión dentro de la función")


funcion2()
print(x, "impresión fuera de la función")