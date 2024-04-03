import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def getAllActores():
    peticion = requests.get("http://172.16.100.114:5503")
    data = json.loads(peticion.text)
    return data


def crearActores():
#Expresiones regulares para los datos ingresados
    codGenero = shortuuid.random(length=4)
    nuevoId = id = random.randint(100, 999)
    nombreGeneroR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    rolActR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')

#Obtener los datos del usuario
    nombreAct = validacion.validar_input(nombreGeneroR, "Ingrese el nombre del Actor: ")
    rolAct = validacion.validar_input(rolActR, "Ingrese el rol del Actor: ")

    actorNuevo = {
            
                "id": f"A{id}",
                "nombre": nombreAct,
                "rol": rolAct
            
    }

# json-server storage/actores.json -b 5503
    url = "http://172.16.100.114:5503"
    data = json.dumps(actorNuevo)
    peticion = requests.post(url,data)

    print("Se ha agregado un nu7evo genero a la base de datos")
    return actorNuevo


def listarActores():
    todosAct = []
    for act in getAllActores():
        todosAct.append({ 
            "Id": act.get("id"),
            "Nombre del Género": act.get("nombre"),
            "Rol de la Actriz/ACtor": act.get("rol")
        })
    return todosAct