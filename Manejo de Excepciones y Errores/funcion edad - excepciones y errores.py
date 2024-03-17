import math

def evalEdad(edad):
    
    if edad <0:
        raise TypeError("No se permiten edades negativas") #Con raise, provocamos que se lance un error. 
    #Si tuvieramos más líneas, no seguiría con el resto del código y se para aquí. 

    if edad<=20:
        return "\nEres muy joven"
    elif edad<=40:
        return "\nEres joven"
    elif edad<=65:
        return "\nEres maduro"
    elif edad<=100:
        return "\nVas a vivir eternamente"

print(evalEdad(66))

def raizCuadrada(num1):
    if num1<0:
        raise ValueError("El número no puede ser negativo")
    
    else:
        return math.sqrt(num1)
    

op1 = int(input("\nIntroduce un número: "))

try: 
    print(raizCuadrada(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    
print("Programa terminado.")