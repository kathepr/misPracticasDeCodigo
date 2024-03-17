import re

lista_nombres=["Ana Gómez",
               "María Martín",
               "Sandra López",
               "Sandra Fernandez",
               "Santiago Martín"]

for elemento in lista_nombres:
    if re.findall("^Sandra", elemento): #Encontrar coincidencias. ^ este es para lo que inicia
        print(elemento)


for elemento in lista_nombres:
    if re.findall("Martín$", elemento): #Encontrar coincidencias. $ este es para el final
        print(elemento)