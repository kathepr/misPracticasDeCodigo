#Diccionarios

frutas = {"manzanas": 5,
          "peras":2,
          "naranjas": 4}

print (frutas)

print ("\nCantidad de manzanas con el método get()")
num_manzanas = frutas.get("manzanas")
print (num_manzanas)

print ("\nCantidad de manzanas consultando el valor: ")
num_manzanas = frutas["manzanas"]


#Ejercicio 2:

frutas["bananas"] = 5
print ("Valor agregado a la lista")

