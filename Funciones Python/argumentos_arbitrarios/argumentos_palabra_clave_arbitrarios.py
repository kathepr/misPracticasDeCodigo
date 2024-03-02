#Argumentos palabra clave arbitrarios
# Tambien conocidos como: **kwargs

def imprimir_info(**info): #Los dos asteriscos ( ** ) los colocamos antes del nombre del parametro que vamos a recibir
    
    print(info)
    for clave, valor in info.items():   #Con los dos **, le estamos diciendo a Python que acepte cualquier número de argumentos de palabra clave
        print(f"\n{clave}: {valor}")    #Y los empaquete en un diccionario. 





imprimir_info(nombre="Juan", edad=25, ciudad="Bogotá")