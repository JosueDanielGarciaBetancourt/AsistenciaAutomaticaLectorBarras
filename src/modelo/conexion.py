import os
import sqlite3


class Conexion:
    def __init__(self):
        try:
            self.rutaActual = os.path.dirname(__file__)
            self.con = sqlite3.connect(f"{self.rutaActual}\DB_Asistencias.db")
            self.crearTablasDB()
            self.crearDocentes()
            """if not self.verificarTablasCreadas():
                    print("Creando tablas")
                    self.crearTablasDB()
                    self.crearDocentes()"""
            print("Conexión establecida con", self.con)
        except sqlite3.Error as e:
            print("Error al conectar a la base de datos:", e)
            print("No se pudo establecer la conexión. Creando una nueva base de datos...")
            self.crearBaseDatos()

    def crearBaseDatos(self):
        try:
            # Conexión a la base de datos (crea la base de datos si no existe)
            self.con = sqlite3.connect(f"{self.rutaActual}\DB_Asistencias.db")
            print("Base de datos creada")
            self.crearTablasDB()
            self.crearDocentes()  # Creación de datos para Testing
        except Exception as ex:
            print("Excepción al crear la base de datos:", ex)
            raise ex

    def eliminarBDExistente(self):
        try:
            self.con.close()  # Cerrar la conexión antes de eliminar la base de datos
            os.remove("src/modelo/DB_Asistencias.db")
            print("Base de datos existente eliminada correctamente")
        except FileNotFoundError:
            print("No se encontró la base de datos existente")
        except Exception as ex:
            print("Error al eliminar la base de datos existente:", ex)

    def crearTablasDB(self):
        sql_create_table_estudiantes = """ CREATE TABLE IF NOT EXISTS tblEstudiantes (
                                estuDni VARCHAR(10) UNIQUE PRIMARY KEY,
                                estuNombre VARCHAR(255) NOT NULL, 
                                estuApellidoPaterno VARCHAR(255),
                                estuApellidoMaterno VARCHAR(255),
                                estuCorreo VARCHAR(255)) """
        
        sql_create_table_docentes = """ CREATE TABLE IF NOT EXISTS tblDocentes (
                                docenteDni VARCHAR(10) UNIQUE PRIMARY KEY,
                                docenteNombre VARCHAR(255) NOT NULL, 
                                docenteApellidoPaterno VARCHAR(255) NOT NULL,
                                docenteApellidoMaterno VARCHAR(255),
                                docentePais VARCHAR(255),
                                docenteCiudad VARCHAR(255),
                                docenteCorreo VARCHAR(255),
                                docenteContraseña VARCHAR(255) NOT NULL,
                                docenteFotoPerfil VARCHAR(255)) """

        
        sql_create_table_cursos = """ CREATE TABLE IF NOT EXISTS tblCursos (
                                cursoId VARCHAR(5) UNIQUE PRIMARY KEY,
                                cursoNombre VARCHAR(255) NOT NULL, 
                                cursoCredito INTEGER) """
        
        sql_create_table_aulas = """ CREATE TABLE IF NOT EXISTS tblAulas (
                                aulaId VARCHAR(5) UNIQUE PRIMARY KEY,
                                aulaPabellon VARCHAR(5) NOT NULL, 
                                aulaSalon VARCHAR(5),
                                aulaCapacidad INTEGER) """
        
        sql_create_table_secciones = """ CREATE TABLE IF NOT EXISTS tblSecciones (
                                nrc VARCHAR(5) UNIQUE PRIMARY KEY,
                                seccionPeriodo VARCHAR(6) NOT NULL, 
                                cursoId VARCHAR(5) NOT NULL,
                                FOREIGN KEY (cursoId) REFERENCES tblCursos(cursoId)) """

        sql_create_table_detalle_estudiantes_secciones= """ CREATE TABLE IF NOT EXISTS tblDetalle_Estudiantes_Secciones (
                                estuDni VARCHAR(10) NOT NULL,
                                nrc VARCHAR(5) NOT NULL,
                                det_estu_seccion_estadoAsistencia BIT NOT NULL,
                                det_estu_seccion_fechaAsistencia DATE NOT NULL,
                                det_estu_seccion_horaAsistencia TIME NOT NULL,
                                FOREIGN KEY (estuDni) REFERENCES tblEstudiantes(estuDni),
                                FOREIGN KEY (nrc) REFERENCES tblSecciones(nrc)) """

        sql_create_table_detalle_secciones_aulas= """ CREATE TABLE IF NOT EXISTS tblDetalle_Secciones_Aulas (
                                aulaId VARCHAR(5) NOT NULL,
                                nrc VARCHAR(5) NOT NULL,
                                det_seccion_aula_horaInicio TIME NOT NULL,
                                det_seccion_aula_horaFin TIME NOT NULL,
                                det_seccion_aula_diaSemana VARCHAR(10) NOT NULL,
                                FOREIGN KEY (aulaId) REFERENCES tblAulas(aulaId),
                                FOREIGN KEY (nrc) REFERENCES tblSecciones(nrc)) """
        
        sql_create_table_detalle_secciones_docentes= """ CREATE TABLE IF NOT EXISTS tblDetalle_Secciones_Docentes (
                                docenteDni VARCHAR(10) NOT NULL,
                                nrc VARCHAR(5) NOT NULL,
                                FOREIGN KEY (docenteDni) REFERENCES tblDocentes(docenteDni),
                                FOREIGN KEY (nrc) REFERENCES tblSecciones(nrc)) """
        curs = self.con.cursor()
        curs.execute(sql_create_table_estudiantes)
        curs.execute(sql_create_table_docentes)
        curs.execute(sql_create_table_cursos)
        curs.execute(sql_create_table_aulas)
        curs.execute(sql_create_table_secciones)
        curs.execute(sql_create_table_detalle_estudiantes_secciones)
        curs.execute(sql_create_table_detalle_secciones_aulas)
        curs.execute(sql_create_table_detalle_secciones_docentes)
        curs.close()


    def crearEstudiantes(self):
        try:
            sql_insert = """ INSERT INTO tblEstudiantes (estDNI, estNombre, estApellidos) VALUES (
                                     '77043114', 
                                     'Josué',
                                     'García Betancourt') """
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
        except sqlite3.IntegrityError:
            print("Ya se creó este estudiante")
        except Exception as ex:
            print("Error al insertar estudiante:", ex)

    def crearDocentes(self):
        try:
            cur = self.con.cursor()

            sql_insert = """INSERT INTO tblDocentes 
                        (docenteDni, docenteNombre, docenteApellidoPaterno, docenteApellidoMaterno, 
                        docentePais, docenteCiudad, docenteCorreo, docenteContraseña) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""

            docentes = [
                ('41280062', 'Judith', 'Camarena', 'Flores', 'Perú', 'Huancayo', 'jcamarenaf@continental.edu.pe', '123'),
                ('19821000', 'Meliton Julio', 'Rosales', 'Pecho', 'Perú', 'Huancayo', 'mrosales@continental.edu.pe', '123')
            ]

            cur.executemany(sql_insert, docentes)
            self.con.commit()
        except sqlite3.IntegrityError:
            print("Ya se creó este docente")
        except Exception as ex:
            print("Error al Insertar Docente:", ex)

    def verificarTablasCreadas(self):
        cursor = self.con.cursor()
        cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name IN 
                       ('tblEstudiantes', 'tblDocentes', 'tblCursos', 'tblAulas', 'tblSecciones',
                       'tblDetalle_Estudiantes_Secciones','tblDetalle_Secciones_Aulas', 'tblDetalle_Secciones_Docentes')""")
        tablas_existentes = [tabla[0] for tabla in cursor.fetchall()]

        if len(tablas_existentes) == 8:
            print("Tablas Existentes Verificadas")
            return True
        else:
            print("Tablas no encontradas ...")
            return False

    # Funcion para Testear Datos (Quitar en las Pruebas Finales)
    def Verdatos(self):
        QueryDatosEstudiantes = "Select * From tblEstudiantes"
        QueryDatosDocentes = "Select * From tblDocentes"
        QueryDatosCursos = "Select * From tblCursos"
        cursorActivo = self.con.cursor()
        cursorActivo.execute(QueryDatosEstudiantes)
        datosEstudiantes = cursorActivo.fetchall()

        cursorActivo.execute(QueryDatosDocentes)
        datosDocentes = cursorActivo.fetchall()

        cursorActivo.execute(QueryDatosCursos)
        datosCursos = cursorActivo.fetchall()

        print("DATOS DE ESTUDIANTES: ")
        for fila in datosEstudiantes:
            print(fila)
        print("DATOS DE DOCENTES: ")
        for fila in datosDocentes:
            print(fila)
        print("DATOS DE CURSOS: ")
        for fila in datosCursos:
            print(fila)

        cursorActivo.close()

    @staticmethod
    def conectar():
        return sqlite3.connect("src/modelo/DB_Asistencias.db")
