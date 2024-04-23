print ("Calculadora de una sola variable \n")
print ("********************************")
print ("      * Menú de opciones *")
print ("********************************")
print("""
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. División entera
    6. Exponente / Potenciación
    7. Módulo / Resto / Residuo \n""")

opcion = int(input("Introduce la opción deseada: "))

if opcion == 1:
    
    print ("Elegiste suma \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero += (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado de la suma es: ", numero)


elif opcion ==2:   
    print ("Elegiste resta \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero -= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado de la resta es: ", numero)


elif opcion == 3:
    print ("Elegiste multiplicación \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero *= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado de la multiplicación es: ", numero)



elif opcion == 4:
    print ("Elegiste división \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero /= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado de la división es: ", numero)



elif opcion == 5:
    print ("Elegiste división entera \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero //= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado de la división entera es: ", numero)



elif opcion ==6:
    print ("Elegiste exponente/potenciación \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero **= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado del exponente / potenciación es: ", numero)




elif opcion ==7:
    print ("Elegiste modulo / resto / residuo \n")

    numero = (int (input ("Introduce el primer número: ")))
    numero %= (int (input ("Introduce el segundo número: ")))
    print ("\n")
    print ("El resultado del modulo / resto / residuo es: ", numero)


else:
    print ("La opción elegida no existe, por favor intentelo de nuevo.")



