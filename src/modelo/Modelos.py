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

    def getName(self):
        return self._nombre


class Seccion:
    def __init__(self, NRC="", periodo="", IDCurso=""):
        self._NRC = NRC
        self._periodo = periodo
        self._IDCurso = IDCurso

    def getNRC(self):
        return self._NRC


class Estudiante:
    def __init__(self, DNI="", nombre="", apellidoPaterno="", apellidoMaterno="", correo=""):
        self._DNI = DNI
        self._nombre = nombre
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._correo = correo

    def getEstudianteAttributes(self):
        return self._DNI, self._nombre, self._apellidoPaterno, self._apellidoMaterno, self._correo

    def getDNI(self):
        return self._DNI