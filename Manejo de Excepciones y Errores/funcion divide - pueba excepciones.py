def divide():
        while True:
            try:
                op1 = float(input("\nIntroduce el primer número: "))
                op2 = float(input("Introduce el segundo número: "))
                print(f"La división es: {op1/op2}")
                break
        
            except ValueError:
                print("Solo se permiten números enteros. Vuelve a intentarlo. ")
            except ZeroDivisionError:
                print("No se puede dividir entre 0. Vuelve a intentarlo.")

            finally: #Lo que se meta en finally, se ejecuta siempre
                 print("Calculo finalizado")


divide()