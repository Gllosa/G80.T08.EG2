import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest


class AccessManager:
    def __init__(self):
        pass

    def ValidateDNI(self, DNI):
        strNumberDni = DNI[0:-1]
        # Comprobar que el dni tiene 8 numeros seguidos de una letra
        if len(strNumberDni) != 8:
            return False
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for char in strNumberDni:
            if int(char) not in numbers:
                return False
        letters = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                   "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        index = int(strNumberDni) % 23
        return letters[index] == DNI[-1].upper()

    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            idDoc = DATA["id"]
            name = DATA["name"]
            req = AccessRequest(idDoc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateDNI(idDoc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req
