#Es muy importante saber en que ambito está nuestra variable        

y=5 #ambito global

def exterior():
    a=50 #ambito local

    def interior():
        nonlocal a 
        a=20 #esta no es una variable global, pero tampoco es local
             #Si yo quiero modificar este tipo de variable, debo ponerle nonlocal al comienzo
             #funcion con variable que está dentro de otra funcion, tenemos variable de ambitos encerrados
    
    interior ()
    print(a) 
    

exterior() #Aquí hago el llamado de la función principal.
