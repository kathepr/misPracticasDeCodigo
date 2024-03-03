# SIRVE PARA TRABAJAR EN PROGRAMACIÓN ORIENTADA A OBJETOS.

def saludar(nombre):
    return f"\nHola, {nombre}\n"


mi_funcion = saludar #Aquí NO estamos llamando a la función, sino que solo estamos creando una referencia a la funcion
                     # No le ponemos parentesis para que sea tratada como objeto
                     # Uso una variable, para tratar a la función como objeto


mensaje = mi_funcion("Ana") #Esta variable se va a comportar como la función si le coloco los parentesis
                            #Aquí actua como si estuviera llamando a la función

print (mensaje)