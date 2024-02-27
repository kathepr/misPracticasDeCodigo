dictionary = {"a": 1,
              "b": 2,
              "c": 3}

print (dictionary)
print (f"\nLOs valores del diccionario son: \n{dictionary.values()}")

print("\nConvirtiendo los valores a lista utilizando list ()")
list_values=list(dictionary.values())

print(f"La lista es: {list_values:}")
print(f"POsición 1 de la lista values: {list_values[1]}")