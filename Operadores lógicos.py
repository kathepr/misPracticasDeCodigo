#Conjunción: and

print ("Operador lógico: and")

num1 = int(input ("Escriba un número mayor a 2 y menor a 5: "))

if num1>2 and num1<5:
    print ("El número ",num1, " cumple con la condición.\n") # \n es un salto de línea, para que no se amontone todo.
else:
    print ("El número ", num1, " no cumple con la condición. \n")


# Disyunción : or

print ("Operador lógico: or")

palabra = input ("Para cumplir la condición escribe 'si' o 'yes': ")
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
    print ("La condición se ha cumplido. \n")

else:
    print ("La condición no se ha cumplido.\n") 




# Negación: nor       

print ("Operador lógico: not")

num1 = int(input("Introduce un número igual a 5: "))

if not num1!=5:
    print ("La condición se cumple.\n")

else:
    print ("La condición no se cumple.")