#Para la entrada de datos, se hace uso del comando #input
# LO PRIMERO QUE HACEMOS ES DECLARAR UNA VARIABLE
# Luego usamos input
palabra = input ("Introduce una palabra: ")

num = int (input ("Introduce un número entero: ")) 
#Es importante colocar int, para que el programa sepa que es un dato numerico entero
#Y que no es una cadena / string

numFloat = float (input ("Introduce un número flotante: "))
#float es para un número flotante

numComplex = complex (input("Introduce un número complejo: "))
#complex es para números complejos

print ("String: ", palabra)
print ("Entero: ", num)
print ("Flotante: ", numFloat)
print ("Número complejo: ", numComplex)
