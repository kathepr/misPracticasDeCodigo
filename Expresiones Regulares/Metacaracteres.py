import re

lista_nombres=["Ana Gómez",
               "María Martín",
               "Sandra López",
               "Sandra Fernandez",
               "Santiago Martín",
               "Susana Martin",
               "niños",
               "niñas"
               ]

print("\nEncontrando coincidencias al inicio usando ^")
for elemento in lista_nombres:
    if re.findall("^Sandra", elemento): #Encontrar coincidencias. ^ este es para lo que inicia
        print(elemento)                 #findall () Encuentra todas las subcadenas de caracteres donde coincide la RE y las retorna como una lista.

print("\nEncontrando coincidencias al final usando $")
for elemento in lista_nombres:
    if re.findall("Martín$", elemento): #Encontrar coincidencias. $ este es para el final
        print(elemento)                 #findall () Encuentra todas las subcadenas de caracteres donde coincide la RE y las retorna como una lista.

print("\nBuscando palabras con caracteres especificos")
for elemento in lista_nombres:
    if re.findall("[S]", elemento): #Buscar en toda la lista, si se encuentra el caracter
        print(elemento) 

print("\nBuscando palabras con caracteres especificos, variantes en una letra")
for elemento in lista_nombres:
    if re.findall("niñ[oa]s", elemento):
        print(elemento)

print("\nBuscando palabras con caracteres especificos, variantes en una letra")
for elemento in lista_nombres:
    if re.findall("Mart[ií]n", elemento):
        print(elemento)