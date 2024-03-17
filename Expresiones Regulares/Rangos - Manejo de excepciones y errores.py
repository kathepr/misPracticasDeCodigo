import re

lista_nombres = ["Ana",
                 "Pedro",
                 "Mería",
                 "Rosa",
                 "Sandra",
                 "Celia",
                 "Ma1",
                 "Ma2",
                 "Ba1",
                 "Ma3",
                 "Va1",
                 "Va2",
                 "Ma4",
                 "Ma5",
                 "MaA",
                 "MaB",
                 "MaC",
                 "Ma.1",
                 "Ma:3",
                 "Ma.5",
                 "Ma:C"
                 ]

print("\nRangos de Números y letras")
for elemento in lista_nombres:
    if re.findall("Ma[.:]", elemento):
        print(elemento)

print("\nRangos de Números y letras")
for elemento in lista_nombres:
    if re.findall("Ma[0-3A-B]", elemento):
        print(elemento)

print("\nRangos de Números y letras")
for elemento in lista_nombres:
    if re.findall("Ma[0-3]", elemento):
        print(elemento)

print("\nRangos de Números y letras")
for elemento in lista_nombres:
    if re.findall("Ma[^0-3]", elemento): #Si quiero obtener algo diferente uso ^
        print(elemento)

print("\nRangos")
for elemento in lista_nombres:
    if re.findall("[o-t]", elemento): #Nos devolvera todo aquello que esté entre la O y la T
        print(elemento)