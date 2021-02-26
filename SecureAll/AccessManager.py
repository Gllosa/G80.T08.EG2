""" Creado por: UC3M
    Fecha de mod.: 20/02/2021"""
import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

# Clase de acceso manager
class AccessManager:
    # Metodo init
    def __init__(self):
        self.dni = None

    # Metodo que valida el DNI
    def validateDNI(self, dni):
        self.dni = dni
        str_number_dni = dni[0:-1]
        # Comprobar que el dni tiene 8 numeros seguidos de una letra
        if len(str_number_dni) != 8:
            return False
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in str_number_dni:
            if int(char) not in numbers:
                return False
        letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                   "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        index = int(str_number_dni) % 23
        return letters[index] == dni[-1].upper()

    # Metodo que lee el acceso desde el JSON
    def readaccessrequestfromJSON(self, argument):

        try:
            with open(argument) as variable_one:
                data = json.load(variable_one)
        except FileNotFoundError as variable_two:
            raise AccessManagementException("Wrong file or file path") from variable_two
        except json.JSONDecodeError as variable_two:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from variable_two

        try:
            id_doc = data["id"]
            name = data["name"]
            req = AccessRequest(id_doc, name)
        except KeyError as variable_two:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from variable_two
        if not self.validateDNI(id_doc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req
