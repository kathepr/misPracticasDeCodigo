fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables] # lista anidada

print(dirty_dozen[0]) # lista fruits
print(dirty_dozen[1]) #lista vegetables

print(" ")
print(dirty_dozen[1][2]) # El primer número es la posición de la lista anidada, el segundo número es el index del elemento que está dentro de la lista. 
print(dirty_dozen[1][3])