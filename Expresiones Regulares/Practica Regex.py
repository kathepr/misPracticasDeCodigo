#Lo primero que hay que hacer para trabajar con expresiones regulares es importar re
import re

cadena = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"
textoBuscar = "Python"
#print(re.search("aprender", cadena)) #Buscar una palabra especifica dentro de una variable

textoEncontrado = re.search(textoBuscar, cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())
print(re.findall(textoBuscar, cadena))
print(len(re.findall(textoBuscar, cadena))) #len, me cuenta cuantas veces está la palabra buscada

# if re.search(textoBuscar, cadena) is not None:
#     print("\nHe encontrado el texto")

# else:
#     print("\nNo he encontrado el texto")