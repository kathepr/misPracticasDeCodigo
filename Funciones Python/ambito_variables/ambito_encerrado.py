#Ocurre cuando una función define a otra función dentro de ella
#Tendríamos una función exterior y una función interior

#La función interior puede acceder a las variables de la función exterior. 

#Podemos definir funciones dentro de otra función: FUNCIONES ANIDADAS


def exterior():
    a=50 # 'a' es de ambito local de la funcion exterior

    def interior():
        print(a) #interior puede acceder a la variable de la funcion exterior


    interior () #Este llamado a la función, ya salió de la parte interior
                #Ahora hace parte de la función exterior
                #Es posible llamar a funciones dentro de otras funciones
    

exterior() #Aquí hago el llamado de la función principal.
