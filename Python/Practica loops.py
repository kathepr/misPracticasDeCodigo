#LOOPS

# Primer tipo de LOOP
# for item in list_of_items:
#     Do something to each item

fruits = ["apple", "peach", "pear"]

for item in fruits: #Ayuda para pasar por todos los elementos de una lista
    print(item)
    print(item + " pie")



#Segundo Tipo de LOOP
# for number in range(1,10):
#     print(number)

print("\nFor con Range\n")

for number in range(1,10):
    print(number) #No imprime el ultimo digito. Si quiero que el 10 se imprima, debo poner el rango en 11

print("\nFor con Range y número extra\n")

for number2 in range(2, 11, 2): #Para que se vaya de dos en dos, debo poner un tercer número, en este caso, dos
    print(number2)

print("\nSuma de numeros del 1 al 100\n")
total = 0
for number100 in range(1, 101):
    total += number100

print(total)
