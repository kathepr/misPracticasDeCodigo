print ("=============")
print ("  CONVERSOR")
print ("=============")

print ("Menú de opciones:")

print ("Presiona 1 para convertir de número a palabra.")
print ("Presiona 2 para convertir de palabra a número.")

opcion = int(input("¿Cúal es tu opción deseada? "))

if opcion == 1:
    num = int (input ("Ingrese el número que desea convertir a palabra: "))
    
    if num == 1:
        print ("El número es 'UNO'.")

    elif num == 2:
        print ("El número es 'DOS'.")

    elif num == 3:
        print ("El número es 'TRES'.") 

    elif num == 4:
        print ("EL número es 'CUATRO'.")   

    elif num == 5:
        print ("El número es 'CINCO'.") 

    else:
        print ("Este programa sólo convierte hasta el número 5.")           
        
elif opcion == 2:
    palabra = input ("Ingrese la palabra que desea convertir a número: ")
    palabra = palabra.lower() #La opción .lower() convierte las palabras en minusculas. De tal forma que si el usuario ingresa mayusculas, automaticamente
                            #el programa lo convertirá a minusculas y podrá ser procesado.

    if palabra == "uno":
        print ("El número es '1'.")

    elif palabra == "dos":
        print ("El número es '2'. ")
    
    elif palabra == "tres":
        print ("El número es '3'.")

    elif palabra == "cuatro":
        print ("El número es '4'.")    

    elif palabra == "cinco":
        print ("El número es '5'.")

    else:
        print ("Este programa solo convierte hasta la palabra 'CINCO'.")    

else:
    print ("La opción ",opcion, " no está disponible.")

print ("Fin.")





