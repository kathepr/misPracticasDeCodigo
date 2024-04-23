#Ejemplo sentencia break:
print("Ciclo while con sentencia break: \n")

contador = 0

while contador < 10:
    contador += 1
    

    if contador == 5:   #Si contador es igual a 5, sale del ciclo y detiene ejecución del while
        break
    print ("Valor actual de la variable: ", contador )
   

print ("Fin del programa, la sentencia break se ha ejecutado.")






#Ejemplo sentencia continue:
print("\nCiclo while con sentencia continue: \n")

contador = 0

while contador < 10:
    contador += 1
    

    if contador == 5:   #Condición: Si contador es igual a 5, no va a imprimir la línea de código que se muestra a continuación.
        continue        #Se la salta y sigue con el resto del ciclo.
    print ("Valor actual de la variable: ", contador )