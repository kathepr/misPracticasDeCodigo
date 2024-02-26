#Ejemplo sentencia break:
print("Ciclo while con sentencia break: \n")

contador = 0

while contador < 10:
    contador += 1
    print ("Valor actual de la variable: ", contador )

    if contador == 5:   #Si contador es igual a 5, sale del ciclo y detiene ejecución del while
        break
   

print ("Fin del programa, la sentencia break se ha ejecutado.")