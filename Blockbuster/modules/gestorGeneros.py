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
    codGenero = shortuuid.random(length=4)
    nuevoId = id = random.randint(100, 999)
    nombreGeneroR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')

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

    print("Se ha agregado un nu7evo genero a la base de datos")
    return generoNuevo


def listarGeneros():
    todosGeneros = []
    for genero in getAllGeneros():
        todosGeneros.append({ 
            "Id": genero.get("id"),
            "Nombre del Género": genero.get("nombre")
        })
    return todosGeneros