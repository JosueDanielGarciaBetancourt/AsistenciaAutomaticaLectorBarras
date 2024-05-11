from src.modelo.Docente import Docente
from src.modelo.conexion import Conexion


class DocenteData:
    def __init__(self):
        self.cursor = None
        self.db = None

    def cerrarConexion(self):
        self.cursor.close()
        self.db.close()

    def login(self, docente: Docente):
        self.db = Conexion.conectar()
        self.cursor = self.db.cursor()
        buscarDocenteUsername = self.cursor.execute(
            "SELECT * FROM tblDocentes "
            "WHERE docenteCorreo ='{}'".format(docente.getUsername()))
        firstRowUsername = buscarDocenteUsername.fetchone()

        if firstRowUsername:  # Existe el nombre de usuario
            buscarDocentePassword = self.cursor.execute(
                "SELECT * FROM tblDocentes "
                "WHERE docenteCorreo = '{}' AND docenteContraseña = '{}'".format(docente.getUsername(), docente.getPassword()))
            paswordRow = buscarDocentePassword.fetchone()
            if paswordRow:  # Contraseña sí coincide
                docente = Docente(paswordRow[0],
                                  paswordRow[1],
                                  paswordRow[2],
                                  paswordRow[3],
                                  paswordRow[4])
                self.cerrarConexion()
                return docente  # Retornar objeto docente con los atributos correctos
            else:  # Contraseña no coincide con el usuario
                docente = Docente(None, None, None, None, None)  # contraseña incorrecta
                self.cerrarConexion()
                return docente
        else:  # No existe el nombre de usuario del docente
            self.cerrarConexion()
            return None
