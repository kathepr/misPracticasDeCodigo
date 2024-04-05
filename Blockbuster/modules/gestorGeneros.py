import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def getAllGeneros():
    peticion = requests.get("http://172.16.100.114:5502")
    data = json.loads(peticion.text)
    return data


def crearGenero():
#Expresiones regulares para los datos ingresados
    nombreGeneroR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    id =''.join(random.choices('0123456789', k=3)) #con random creo una secuencia aleatoria de elementos, join me ayuda a convertir la lista en caracteres
    nuevoNroFormulario =  shortuuid.random(length=4) #uuid me ayuda a generar un id unico y aleatorio


#Obtener los datos del usuario
    nombreGenero = validacion.validar_input(nombreGeneroR, "Ingrese el nombre del género: ")

    generoNuevo = {
            
                "id": f"G{id}",
                "nombre": nombreGenero
            
    }

# json-server storage/generos.json -b 5502
    url = "http://172.16.100.114:5502"
    data = json.dumps(generoNuevo)
    peticion = requests.post(url,data)

    print("\nSe ha agregado un nuevo genero a la base de datos")
    return generoNuevo


def listarGeneros():
    todosGeneros = []
    for genero in getAllGeneros():
        generoInfo = { 
            "Id": genero.get("id"),
            "Nombre del Género": genero.get("nombre")
        }
        todosGeneros.append(generoInfo) #Guardo en una lista toda la información que me brindó el loop por la base de datos de Genero
    return todosGeneros