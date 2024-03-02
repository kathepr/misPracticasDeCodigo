#La función recursiva, es una función que se llama así misma

def contar_hasta_cero(n):
    
    if n<=0:
        print("He llegado a cero!") #El condicional es el caso base que va a impedir que se cree un buble infinito
    else:
        print(n)
        n=n-1
        contar_hasta_cero(n)   #La función se está llamando así misma durante su ejecución
                               #Es necesario definir un caso base en este tipo de funciones
                               #De lo contrario, mandará error porque se crea un ciclo infinito
                        



contar_hasta_cero(5)