""" Colaboradores: UC3M, Gonzalo Llosa, Diego Robles
    Fecha: 26/02/2021"""

import json
from datetime import datetime

# Clase de peticion de acceso
class AccessRequest:
    # Metodo init
    def __init__(self, idDocument, fullName):
        self.privName = fullName
        self.privIdDocument = idDocument
        justnow = datetime.utcnow()
        self.timeStamp = datetime.timestamp(justnow)
    # Metodo para reconocer clase como string
    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    # Getter de name
    @property
    def name(self):
        return self.privName

    # Setter de name
    @name.setter
    def name(self, value):
        self.privName = value

    # Getter de idDocument
    @property
    def idDocument(self):
        return self.privIdDocument

    # Setter de idDocument
    @idDocument.setter
    def idDocument(self, value):
        self.privIdDocument = value
