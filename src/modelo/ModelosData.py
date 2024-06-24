from src.modelo.Modelos import Docente, Seccion, Estudiante
from src.modelo.conexion import Conexion


class DocenteData:
    def __init__(self):
        self.con = None
        self.cursor = None

    def iniciarConexion(self):
        try:
            self.con = Conexion.conectar()
            self.cursor = self.con.cursor()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
        
    def cerrarConexion(self):
        self.cursor.close()
        self.con.close()

    def getDocenteData(self, docente: Docente):
        
        self.iniciarConexion()

        buscarDocenteUsername = self.cursor.execute(
            "SELECT * FROM tblDocentes "
            "WHERE docenteCorreo ='{}'".format(docente.getUsername()))
        firstRowUsername = buscarDocenteUsername.fetchone()

        if firstRowUsername:  # Existe el nombre de usuario
            buscarDocentePassword = self.cursor.execute(
                "SELECT * FROM tblDocentes "
                "WHERE docenteCorreo = '{}' AND docenteContraseña = '{}'".format(docente.getUsername(),
                                                                                 docente.getPassword()))
            datosDocente = buscarDocentePassword.fetchone()
            if datosDocente:  # si la consulta funciona significa que existe el usuario con su contraseña ingresada
                docente = Docente(datosDocente[0],
                                  datosDocente[1],
                                  datosDocente[2],
                                  datosDocente[3],
                                  datosDocente[4],
                                  datosDocente[5],
                                  datosDocente[6],
                                  datosDocente[7],
                                  datosDocente[8])
                self.cerrarConexion()
                return docente  # Retornar objeto docente con los atributos correctos
            else:  # Contraseña no coincide con el usuario
                docente = Docente(None, None, None, None, None)  # contraseña incorrecta
                self.cerrarConexion()
                return docente
        else:  # No existe el nombre de usuario del docente
            self.cerrarConexion()
            return None
        
    def getDocenteFotoPerfil(self, docente: Docente):
        self.iniciarConexion()
        
        try:
            self.cursor.execute("SELECT docenteFotoPerfil FROM tblDocentes WHERE docenteDni = '{}'".format(docente._DNI))

            docenteFotoPerfil = self.cursor.fetchall()

            self.cerrarConexion()
            return docenteFotoPerfil[0][0]
        except Exception as e:
            print(f"Error al Obtener Foto de Perfil: {e}")
            return None



class SeccionData:
    def __init__(self):
        self.cursor = None
        self.con = None

    def iniciarConexion(self):
        try:
            self.con = Conexion.conectar()
            self.cursor = self.con.cursor()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def cerrarConexion(self):
        self.cursor.close()
        self.con.close()

    def searchSeccion(self, seccion: Seccion):
        
        self.iniciarConexion()

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
        
    def searchNrcs_by_Docente(self, docente: Docente):
        self.iniciarConexion()
        
        try:
            self.cursor.execute(
                "SELECT nrc FROM tblDetalle_Secciones_Docentes WHERE docenteDni = {}".format(docente._DNI))
            
            nrcs = []
                
            for row in self.cursor.fetchall():
                nrcs.append(str(row[0]))

            self.cerrarConexion()
            return nrcs
        
        except Exception as e:
            print(f"Error al ejecutar la consulta para obtener los NRCs: {e}")
            self.cerrarConexion()
            return None

    def searchCurso_by_NRC(self, NRC):
        self.iniciarConexion()
        try:
            self.cursor.execute(
                """SELECT tblCursos.cursoNombre
                FROM tblCursos
                INNER JOIN tblSecciones ON tblCursos.cursoId = tblSecciones.cursoId
                WHERE tblSecciones.nrc = ?
            """,(NRC,)
            )
            nombre_curso = self.cursor.fetchall()
            return nombre_curso[0][0]
        except Exception as e:
            print(f"Error al ejecutar la consulta para obtener Curso por NRC: {e}")
            self.cerrarConexion()
            return None

    def searchEstudiantes_by_NRC(self, NRC):
        
        self.iniciarConexion()

        try:
            # Obtener los DNIs de los estudiantes por NRC
            self.cursor.execute(
                "SELECT estuDni FROM tblDetalle_Estudiantes_Secciones WHERE nrc = ?",
                (NRC,)
            )
            DNIs = self.cursor.fetchall()
        except Exception as e:
            print(f"Error al ejecutar la consulta para obtener DNIs: {e}")
            self.cerrarConexion()
            return None

        if not DNIs:  # No existen estudiantes con el NRC solicitado
            print(f"No existen estudiantes con el NRC solicitado: {NRC}")
            self.cerrarConexion()
            return None

        listaObjetosEstudiante = []
        for dni in DNIs:
            try:
                valor_dni = dni[0]
                self.cursor.execute(
                    "SELECT * FROM tblEstudiantes WHERE estuDni = ?",
                    (valor_dni,)
                )
                estudianteEncontrado = self.cursor.fetchone()

                if estudianteEncontrado:
                    estudiante = Estudiante(
                        estudianteEncontrado[0], estudianteEncontrado[1],
                        estudianteEncontrado[2], estudianteEncontrado[3],
                        estudianteEncontrado[4]
                    )
                    listaObjetosEstudiante.append(estudiante)
                else:
                    print(f"No se encontró estudiante con DNI {valor_dni}")
            except Exception as e:
                print(f"Error al obtener o procesar los datos del estudiante con DNI {valor_dni}: {e}")

        try:
            self.cerrarConexion()
        except Exception as e:
            print(f"Error al cerrar la conexión a la base de datos: {e}")

        return listaObjetosEstudiante


  # Retornar lista de objetos estudiante con los atributos correctos

    #def insertEstudiantes_by_NRC(self, NRC):
