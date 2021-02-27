""" Colaboradores: UC3M, Gonzalo Llosa, Diego Robles
    Fecha: 26/02/2021"""

# Clase excepcion de acceso
class AccessManagementException(Exception):
    # Metodo init
    def __init__(self, message):
        self.privMessage = message
        super().__init__(self.message)

    # Getter de message
    @property
    def message(self):
        return self.privMessage

    # Setter de message
    @message.setter
    def message(self, value):
        self.privMessage = value
