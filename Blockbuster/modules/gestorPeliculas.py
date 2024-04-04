import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def getAllPeliculas():
    peticion = requests.get("http://172.16.100.114:5504")
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
    nombrePelicula = validacion.validar_input(nombrePeliculaR, "Ingrese el nombre del Actor: ")
    duracion = validacion.validar_input(duracionR, "Ingrese la duración de la pelicula (en minutos): ")
    sinopsis = validacion.validar_input(sinopsisR, "Ingrese la sinopsis de la pelicula: ")
    
    peliculaNueva = {
        "id": id,
        "nombre": nombrePelicula,
        "duracion": duracion,
        "sinopsis": sinopsis,
        "generos":[],
        "actores":[],
        "formato":[]
        }
    
# Crear petición post para agregar la peli a la base de datos

# json-server storage/peliculas.json -b 5504
    url = "http://172.16.100.114:5504"
    data = json.dumps(peliculaNueva)
    peticion = requests.post(url,data)

    print("\nSe ha agregado una pelicula nueva a la base de datos")
    return peliculaNueva