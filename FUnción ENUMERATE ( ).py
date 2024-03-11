frutas = ["manzana", "platano", "uva", "sandia"]
print(frutas)

for posicion, fruta in enumerate(frutas, start = 0):
    print(f"Posición {posicion}: {fruta}")

#COnvertido a lista
enumerado = list(enumerate(frutas, start = 1))
print(enumerado)

#Enumerate permite realizar seguimiento de la posición de los datos. 
#Como : tuplas, listas, strings