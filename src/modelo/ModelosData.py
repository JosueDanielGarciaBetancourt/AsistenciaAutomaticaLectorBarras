from src.modelo.Modelos import Docente, Seccion, Estudiante
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
                "WHERE docenteCorreo = '{}' AND docenteContraseña = '{}'".format(docente.getUsername(),
                                                                                 docente.getPassword()))
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


class SeccionData:
    def __init__(self):
        self.cursor = None
        self.db = None

    def cerrarConexion(self):
        self.cursor.close()
        self.db.close()

    def searchSeccion(self, seccion: Seccion):
        self.db = Conexion.conectar()
        self.cursor = self.db.cursor()
        buscarSeccionNRC = self.cursor.execute(
            "SELECT * FROM tblSecciones "
            "WHERE nrc ='{}'".format(seccion.getNRC()))
        firstNRC = buscarSeccionNRC.fetchone()

        if firstNRC:  # Existe el NRC de la sección
            seccion = Seccion(firstNRC[0],
                              firstNRC[1],
                              firstNRC[2])
            self.cerrarConexion()
            return seccion  # Retornar objeto sección con los atributos correctos
        else:  # No existe el NRC de la sección
            self.cerrarConexion()
            return None

    def searchEstudiantes_by_NRC(self, NRC):
        self.db = Conexion.conectar()
        self.cursor = self.db.cursor()
        buscarDNIEstudiantesByNRC = self.cursor.execute(
            "SELECT estuDni FROM tblDetalle_Estudiantes_Secciones "
            "WHERE nrc ='{}'".format(NRC))

        if buscarDNIEstudiantesByNRC.fetchone() is None:  # No existen estudiantes con el NRC solicitado
            print("No existen estudiantes con el NRC solicitado")
            self.cerrarConexion()
            return None
        else:
            # Consulta para obtener los DNIs de los estudiantes encontrados
            DNIs = buscarDNIEstudiantesByNRC.fetchall()
            listaObjetosEstudiante = []
            for dni in DNIs:  # dni es una tupla, ejem: ('73125046',)
                valor_dni = dni[0]
                buscarEstudianteByDNI = self.cursor.execute(
                    "SELECT * FROM tblEstudiantes "
                    "WHERE estuDni ='{}'".format(valor_dni))
                estudianteEncontrado = buscarEstudianteByDNI.fetchone()
                estudiante = Estudiante(estudianteEncontrado[0], estudianteEncontrado[1], estudianteEncontrado[2],
                                        estudianteEncontrado[3], estudianteEncontrado[4])
                listaObjetosEstudiante.append(estudiante)
            self.cerrarConexion()
            return listaObjetosEstudiante  # Retornar lista de objetos estudiante con los atributos correctos

    #def insertEstudiantes_by_NRC(self, NRC):
