print ("Bienvenido al sistema. \n")
nombre = input ("Por favor, ingrese su nombre: ")
clave = input ("Por favor, ingrese la CLAVE del departamento al que pertenece: ")

if clave == "clave1":
    print ("Usted se encuentra en el Departamento de Atención al Cliente. \n")
    
    
    tiempo = float(input ("¿Cuantos años lleva trabajando en Rappi? "))
    if tiempo >= 1 and tiempo<2:
        print (nombre, ", usted tiene derecho a 6 días de vacaciones.")

    elif tiempo >= 2 and tiempo <= 6:
        print (nombre, ", usted tiene derecho a 14 días de vacaciones.")    
    
    elif tiempo >=7:
        print (nombre, ", usted tiene derecho a 20 días de vacaciones.  ")
    
    else:
        print (nombre, ", aun no tiene derecho a vacaciones.")





elif clave == "clave2":
    print ("Usted se encuentra en el Departamento de Logística. \n")
    
    
    tiempo = float(input ("¿Cuantos años lleva trabajando en Rappi? "))
    if tiempo >= 1 and tiempo<2:
        print (nombre, ", usted tiene derecho a 7 días de vacaciones.")

    elif tiempo >= 2 and tiempo <= 6:
        print (nombre, ", usted tiene derecho a 15 días de vacaciones.")    
    
    elif tiempo >=7:
        print (nombre, ", usted tiene derecho a 22 días de vacaciones.  ")    

    else:
        print (nombre, ", aun no tiene derecho a vacaciones.")    





elif clave == "clave3":
    print ("Usted se encuentra en el Departamento de Gerencia. \n")
    
    
    tiempo = float(input ("¿Cuantos años lleva trabajando en Rappi? "))
    if tiempo >= 1 and tiempo<2:
        print (nombre, ", usted tiene derecho a 10 días de vacaciones.")

    elif tiempo >= 2 and tiempo <= 6:
        print (nombre, ", usted tiene derecho a 20 días de vacaciones.")    
    
    elif tiempo >=7:
        print (nombre, ", usted tiene derecho a 30 días de vacaciones.  ")
    
    else:
        print (nombre, ", aun no tiene derecho a vacaciones.")




else:
    print (nombre, ", la clave del departamento ingresada NO EXISTE, por favor vuelva a intentarlo.")


