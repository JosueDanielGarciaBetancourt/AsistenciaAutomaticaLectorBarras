class Docente:
    def __init__(self, DNI="", nombre="", apellidoPaterno="",apellidoMaterno="" ,
                 pais="" ,ciudad="",correo="", password="", fotoPerfil=""):
        self._DNI = DNI
        self._nombre = nombre
        self._apellidoPaterno = apellidoPaterno
        self._apellidoMaterno = apellidoMaterno
        self._pais = pais
        self._ciudad = ciudad
        self._correo = correo 
        self._password = password
        self._fotoPerfil = fotoPerfil

    def getUsername(self):
        return self._correo

    def getPassword(self):
        return self._password

    def getName(self):
        return self._nombre

    def getPais(self):
        return self._pais

    def getCiudad(self):
        return self._ciudad

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