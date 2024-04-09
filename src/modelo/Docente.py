class Docente:
    def __init__(self, DNI="", nombre="", apellidos="", username="", password=""):
        self._DNI = DNI
        self._nombre = nombre
        self._apellidos = apellidos
        self._username = username
        self._password = password

    def getUsername(self):
        return self._username

    def getPassword(self):
        return self._password


