import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def getAllActores():
    peticion = requests.get("http://172.16.103.20:5503")
    data = json.loads(peticion.text)
    return data


def crearActores():
#Expresiones regulares para los datos ingresados
    codGenero = shortuuid.random(length=4)
    id =''.join(random.choices('0123456789', k=3)) #con random creo una secuencia aleatoria de elementos, join me ayuda a convertir la lista en caracteres
    nombreGeneroR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    rol = re.compile(r"^[1-3]$") # Solo se permite un número entero del 1 al 3

#Obtener los datos del usuario
    nombreAct = validacion.validar_input(nombreGeneroR, "Ingrese el nombre del Actor: ")

    print("""
                    OPCIONES PARA EL TIPO DE ASIGNACIÓN
                          
                          1. PROTAGONISTA
                          2. ANTAGONISTA
                          3. REPARTO 
                    """)
    rol = input("Ingrese el rol de la actriz/actor: ")
    if rol == "1":
        rolAct = "Protagonista"
    elif rol == "2":
        rolAct = "Antagonista"
    elif rol == "3":
        rolAct = "Reparto"
        

    actorNuevo = {
                "id": f"A{id}",
                "nombre": nombreAct,
                "rol": rolAct
                }

# json-server storage/actores.json -b 5503
    url = "http://172.16.103.20:5503"
    data = json.dumps(actorNuevo)
    peticion = requests.post(url,data)

    print("\nSe ha agregado un nuevo actriz/actor a la base de datos")
    return actorNuevo


def listarActores():
    todosActores = []
    for act in getAllActores():
        actoresInfo = { 
            "Id": act.get("id"),
            "Nombre del Género": act.get("nombre"),
            "Rol de la Actriz/Actor": act.get("rol")
        }
        todosActores.append(actoresInfo) #Guardo en una lista toda la información que me brindó el loop por la base de datos de Actores/Actrices
    return todosActores