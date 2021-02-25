""" Atores: UC3M
Fecha de ultima mod.: indeterminada"""

# Clase excepcion de acceso
class AccessManagementException(Exception):
    # Metodo init
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    # Getter de message
    @property
    def message(self):
        return self.message

    # Setter de message
    @message.setter
    def message(self, value):
        self.message = value
