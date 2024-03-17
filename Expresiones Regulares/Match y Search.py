import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María .López"
nombre4="sandra Giraldo"
nombre5="Lara Lopez"
codigo1="dncncñencñ71cnjncncnc"


#Match va a buscar si hay coincidencias en un patrón
print("\nBuscar con search, si existe dentro de toda la cadena un patrón especifico")
if re.search("71", codigo1):
    print("Hemos encontrado el 71")
else:
    print("No hemos encontrado el 71")




print("\nUtilizando match:")
if re.match("Sandra",nombre1):
    print("Hemos encontrado el nombre ", nombre1)
else:
    print("No hemos encontrado el nombre")

print("\nUtilizando match:")
if re.match("Sandra",nombre2):
    print("Hemos encontrado el nombre ")
else:
    print("No hemos encontrado el nombre")

#Para que ignore si hay o no mayusculas:

print("\nUtilizando match y que ignore mayusculas:")
if re.match("Sandra",nombre4, re.IGNORECASE):
    print("Hemos encontrado el nombre ")
else:
    print("No hemos encontrado el nombre")


#Comodin . punto para que ignore un caracter
print("\nUtilizando match y punto para ignorar un caracter:")
if re.match(".ara",nombre5, re.IGNORECASE):
    print("Hemos encontrado el nombre ")
else:
    print("No hemos encontrado el nombre")




cadena1 = "Jara López"
cadena2= "54853685"
cadena3= "a54654654"

print("\nUtilizando match y punto para ignorar un caracter:")
if re.match("\d",cadena1):
    print("Hemos encontrado el número ")
else:
    print("No hemos encontrado el número")