import modules.validaciones as validacion
import shortuuid
import re
import random
import json
import requests

def agregarPelicula():
#Expresiones regulares para los datos ingresados
    nombrePeliculaR = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚ\s]+$')
    duracionR = re.compile(r'^[0-9]+$')
    sinopsis = re.compile(r'^.*$')