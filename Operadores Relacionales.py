print ("Introduce dos números a comparar")
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
print (" ")
print ("Estás son las comparaciones que se cumplen: ")


if num1 == num2:
    print ("* Los números son iguales")

if num1 != num2:
    print ("* Los números son diferentes")

if num1 > num2:
    print ("* El número ", num1, " es mayor que el ", num2)

if num1 >= num2:
    print ("* El número ", num1, " es mayor igual que el ", num2)

if num1 < num2:
    print ("* El número ", num1, " es menor que el ", num2)

if num1 <= num2:
    print ("* EL número ", num1, " es menor o igual que ", num2)