""" Atores: UC3M
Fecha de ultima mod.: indeterminada"""

import json
from datetime import datetime

# Clase de peticion de acceso
class AccessRequest:
    # Metodo init
    def __init__(self, idDocument, fullName):
        self.name = fullName
        self.idDocument = idDocument
        justnow = datetime.utcnow()
        self.timeStamp = datetime.timestamp(justnow)
    # Metodo para reconocer clase como string
    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    # Getter de name
    @property
    def name(self):
        return self.name

    # Setter de name
    @name.setter
    def name(self, value):
        self.name = value

    # Getter de idDocument
    @property
    def idDocument(self):
        return self.idDocument

    # Setter de idDocument
    @idDocument.setter
    def idDocument(self, value):
        self.idDocument = value
