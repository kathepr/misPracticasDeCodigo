import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def getAllFormatos():
    peticion = requests.get("http://172.16.100.114:5504")
    data = json.loads(peticion.text)
    return data


def crearFormatos():
#Expresiones regulares para los datos ingresados
    codGenero = shortuuid.random(length=4)
    nuevoId = id = random.randint(100, 999)
    nombreFormatoR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    NroCopiasR = re.compile(r'^[0-9]+$')
    valorPrestamoR = re.compile(r'^[0-9]+$')

#Obtener los datos del usuario
    nombreFormato = validacion.validar_input(nombreFormatoR, "Ingrese el nombre del Formato: ")
    NroCopias = int(validacion.validar_input(NroCopiasR, "Ingrese el numero de copias: "))
    valorPrestamo = int(validacion.validar_input(valorPrestamoR, "Ingrese el valor del préstamo: "))

    formatoNuevo = {
            
                "id": f"F{id}",
                "nombre": nombreFormato,
                "NroCopias": NroCopias,
                "valorPrestamo": valorPrestamo
            
    }

# json-server storage/formatos.json -b 5504
    url = "http://172.16.100.114:5504"
    data = json.dumps(formatoNuevo)
    peticion = requests.post(url,data)

    print("Se ha agregado un nu7evo genero a la base de datos")
    return formatoNuevo


def listarFormatos():
    todosFormatos = []
    for formato in getAllFormatos():
        todosFormatos.append({ 
            "Id": formato.get("id"),
            "Nombre del Formato": formato.get("nombre"),
            "Número de Copias": formato.get("NroCopias"),
            "Valor del Prestamo": formato.get("valorPrestamo")
        })
    return todosFormatos