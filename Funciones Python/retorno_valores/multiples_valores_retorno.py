def operaciones_basicas(a, b):
    suma = a + b
    resta= a - b
    multiplicacion = a * b
    division = a/b
    return suma, resta, division, multiplicacion #Aquí se colocan TODOS LOS VALORES QUE QUIERO RETORNAR.


resultados=operaciones_basicas(2, 2)
print(resultados) #Los retorna en forma de tupla