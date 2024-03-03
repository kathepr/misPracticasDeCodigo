
def multiplicador(factor): #Esta función
    def funcion_interna(numero): #Devuelve esta funcion
        return numero * factor
    
    return funcion_interna #No estamos haciendo un llamado a la función, sino que estamos retornando su valor


multiplicar_por_2 = multiplicador(2) #Cuando llamamos a la funcion multiplicador
multiplicar_por_5 = multiplicador(5) #Lo que hemos hecho es personalizar a funcion interna

print(multiplicar_por_2(3))
print(multiplicar_por_5(4))