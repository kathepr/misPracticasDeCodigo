import modules.validaciones as validacion
import modules.gestorGeneros as generos
from tabulate import tabulate
import shortuuid
import re
import random
import json
import requests

def getAllPeliculas():
    peticion = requests.get("http://172.16.100.114:5501")
    data = json.loads(peticion.text)
    return data


def agregarPelicula():
    peliculaNueva = {}
#Expresiones regulares para los datos ingresados
    id =''.join(random.choices('0123456789', k=3)) #con random creo una secuencia aleatoria de elementos, join me ayuda a convertir la lista en caracteres 
    nombrePeliculaR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    duracionR = re.compile(r'^[0-9]+$')
    sinopsisR = re.compile(r'^.*$')

#Obtener los datos del usuario
    nombrePelicula = validacion.validar_input(nombrePeliculaR, "Ingrese el nombre de la pelicula: ")
    duracion = validacion.validar_input(duracionR, "Ingrese la duración de la pelicula (en minutos): ")
    sinopsis = validacion.validar_input(sinopsisR, "Ingrese la sinopsis de la pelicula: ")
    
    peliculaNueva = {
        "id": f"P0{id}",
        "nombre": nombrePelicula,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "generos":[],
        "actores":[],
        "formato":[]
        }
    
# Crear petición post para agregar la peli a la base de datos

# json-server storage/peliculas.json -b 5504
    url = "http://172.16.100.114:5501"
    data = json.dumps(peliculaNueva)
    peticion = requests.post(url,data)

    print("\nSe ha agregado una pelicula nueva a la base de datos")
    return peliculaNueva



def editarPelicula(id):
    peliculaEditada = {}
    peliculaId = []

# json-server storage/peliculas.json -b 5501
    url = f"http://172.16.100.114:5501/{id}"

#Expresiones regulares para los datos ingresados
    nombrePeliculaR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    duracionR = re.compile(r'^[0-9]+$')
    sinopsisR = re.compile(r'^.*$')

#Obtener los datos del usuario
    print("¿Desea editar el nombre de la pelicula?")
    opcionnombre = input(""" 1. SI   /    2. NO   : """)
    if opcionnombre == "1":
        nombrePelicula = validacion.validar_input(nombrePeliculaR, "Edite el nombre de la pelicula: ")
        peliculaEditada = {"nombre": nombrePelicula}
        data = json.dumps(peliculaEditada)
        peticion = requests.patch(url,data)
    elif opcionnombre == "2":
        print(" ")
    
    

    print("¿Desea editar la duración de la pelicula?")
    opcionduracion = input(""" 1. SI   /    2. NO   : """)
    if opcionduracion == "1":
        duracion = validacion.validar_input(duracionR, "Edite la duración de la pelicula (en minutos): ")
        peliculaEditada = {"duracion": duracion}
        data = json.dumps(peliculaEditada)
        peticion = requests.patch(url,data)
    elif opcionduracion == "2":
        print(" ")
    


    print("¿Desea editar la sinopsis de la pelicula?")
    opcionsinopsis = input(""" 1. SI   /    2. NO   : """)
    if opcionsinopsis == "1":
        duracion = sinopsis = validacion.validar_input(sinopsisR, "Edite la sinopsis de la pelicula: ")
        peliculaEditada = {"sinopsis": sinopsis}
        data = json.dumps(peliculaEditada)
        peticion = requests.patch(url,data)
    elif opcionsinopsis == "2":
        print(" ")

    print("¿Desea editar los géneros de la pelicula?")
    opcionsinopsis = input(""" 1. SI   /    2. NO   : """)
    if opcionsinopsis == "1":

        print("""
          
        *******************************
              EDITAR GÉNEROS
        *******************************
          
            1. Agregar género
            2. Eliminar género
            3. Salir
          
          """)
        
        opcionGenero = input("Seleccione la opción que desea: ")
        if opcionGenero == "1":
            print("Estos son los generos disponibles en la base de datos: ")
            todosGeneros = generos.listarGeneros() #Se guarda en esta variable, todos los generos que devuelven la función
            print(tabulate(todosGeneros, headers = "keys", tablefmt="rounded_grid"))#Se imprimen todos los generos en la tabla
            idGenero = input("\nIngrese el id del genero que desea agregar a la pelicula: ")

#                          FALTA AGREGAR EN GENEROS, LA INFO DEL GENERO QUE SELECCIONE EL USUARIO
# -------------------------------------------------------------------------------------------------------------


        # duracion = sinopsis = validacion.validar_input(sinopsisR, "Edite la sinopsis de la pelicula: ")
        # peliculaEditada = {"sinopsis": sinopsis}
        # data = json.dumps(peliculaEditada)
        # peticion = requests.patch(url,data)
    elif opcionsinopsis == "2":
        print(" ")
    
    




#Despues de los cambios que se van haciendo en tiempo real, traigo la información actual de la peli y eso es lo que voy a mostrarle al usuario. 
    peticion = requests.get(f"http://172.16.100.114:5501/{id}")
    datosPelicula = json.loads(peticion.text)

    peliculaActualizada = {
    "Id": datosPelicula["id"],
    "Nombre de la Pelicula": datosPelicula["nombre"],
    "Duracion": datosPelicula["duracion"],
    "Sinopsis": datosPelicula["sinopsis"],
    "Generos": datosPelicula["generos"],
    "Actores": datosPelicula["actores"],
    "Formato": datosPelicula["formato"]
    }
  
    
    print("La pelicula se ha actualizado con la siguiente información: ")
    return peliculaActualizada

    


