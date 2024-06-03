import random

#Número entero aleatorio de 1 al 10 (los incluye)
random_integer = random.randint(1,10)
print(random_integer)


#Decimal aleatorio en 0 y 9,999999
random_float = random.random()
print(random_float)

#Decimal aleatorio de 0 al 5
random_float2 = random.uniform(0,5)
print(random_float2)


#ejemplos
love_score = random.randint(1,100)
print(f"\nYour love score is {love_score}")