dictionary = {"a": 1,   #Cada uno de estos elementos es considerado un item
              "b": 2,   # Hay tres items en este diccionario.
              "c": 3}

print (dictionary)
print (f"\nLos items del diccionario son:\n{dictionary.items()}")

print ("\nConvirtiendo items a lista utilizando el constructor list()")
lista_items = list(dictionary.items())

print (f"La lista es: {lista_items}")
print (f"Posición 1 de la lista items: {lista_items [1]}")
