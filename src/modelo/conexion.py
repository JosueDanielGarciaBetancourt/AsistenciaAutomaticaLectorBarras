import os
import sqlite3


class Conexion:
    def __init__(self):
        try:
            self.rutaActual = os.path.dirname(__file__)
            self.con = sqlite3.connect(f"{self.rutaActual}\DB_Asistencias.db")
            print("Conexión establecida con", self.con)
            self.crearTablasDB()
            self.crearDocentes()
            """if not self.verificarTablasCreadas():
                    print("Creando tablas")
                    self.crearTablasDB()
                    self.crearDocentes()"""
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

    def crearTablas(self):
        sql_create_table1 = """ CREATE TABLE IF NOT EXISTS tblEstudiantes (
                                estDNI TEXT UNIQUE PRIMARY KEY,
                                estNombre TEXT, 
                                estApellidos TEXT) """

        sql_create_table2 = """ CREATE TABLE IF NOT EXISTS tblDocentes (
                                        docDNI TEXT UNIQUE PRIMARY KEY,
                                        docNombre TEXT, 
                                        docApellidos TEXT,
                                        docUsername TEXT UNIQUE,
                                        docPassword TEXT) """

        sql_create_table3 = """ CREATE TABLE IF NOT EXISTS tblCursos (
                                curNRC TEXT UNIQUE PRIMARY KEY,
                                curNombre TEXT,
                                curAula TEXT) """
        curs = self.con.cursor()
        curs.execute(sql_create_table1)
        curs.execute(sql_create_table2)
        curs.execute(sql_create_table3)
        curs.close()
        self.crearEstudiantes()
        self.crearDocentes()

    def crearTablasDB(self):
        sql_create_table_estudiantes = """ CREATE TABLE IF NOT EXISTS tblEstudiantes (
                                estuDni TEXT UNIQUE PRIMARY KEY,
                                estuNombre TEXT NOT NULL, 
                                estuApellidoPaterno TEXT,
                                estuApellidoMaterno TEXT,
                                estuCorreo TEXT) """

        sql_create_table_docentes = """ CREATE TABLE IF NOT EXISTS tblDocentes (
                                docenteDni TEXT UNIQUE PRIMARY KEY,
                                docenteNombre TEXT NOT NULL, 
                                docenteApellidoPaterno TEXT NOT NULL,
                                docenteApellidoMaterno TEXT,
                                docentePais TEXT,
                                docenteCiudad TEXT,
                                docenteCorreo TEXT,
                                docenteContraseña TEXT NOT NULL) """

        sql_create_table_cursos = """ CREATE TABLE IF NOT EXISTS tblCursos (
                                cursoId TEXT UNIQUE PRIMARY KEY,
                                cursoNombre TEXT NOT NULL, 
                                cursoCredito INTEGER) """

        sql_create_table_aulas = """ CREATE TABLE IF NOT EXISTS tblAulas (
                                aulaId TEXT UNIQUE PRIMARY KEY,
                                aulaPabellon TEXT NOT NULL, 
                                aulaSalon TEXT,
                                aulaCapacidad INTEGER) """

        sql_create_table_secciones = """ CREATE TABLE IF NOT EXISTS tblSecciones (
                                nrc TEXT UNIQUE PRIMARY KEY,
                                seccionPeriodo TEXT NOT NULL, 
                                cursoId TEXT NOT NULL,
                                FOREIGN KEY (cursoId) REFERENCES tblCursos(cursoId)) """

        sql_create_table_detalle_estudiantes_secciones = """ CREATE TABLE IF NOT EXISTS tblDetalle_Estudiantes_Secciones (
                                estuDni TEXT NOT NULL,
                                nrc TEXT NOT NULL,
                                det_estu_seccion_estadoAsistencia TEXT NOT NULL,
                                det_estu_seccion_fechaAsistencia TEXT NOT NULL,
                                FOREIGN KEY (estuDni) REFERENCES tblEstudiantes(estuDni),
                                FOREIGN KEY (nrc) REFERENCES tblSecciones(nrc)) """

        sql_create_table_detalle_secciones_aulas = """ CREATE TABLE IF NOT EXISTS tblDetalle_Secciones_Aulas (
                                aulaId TEXT NOT NULL,
                                nrc TEXT NOT NULL,
                                det_seccion_aula_horaInicio TEXT NOT NULL,
                                det_seccion_aula_horaFin TEXT NOT NULL,
                                det_seccion_aula_diaSemana TEXT NOT NULL,
                                FOREIGN KEY (aulaId) REFERENCES tblAulas(aulaId),
                                FOREIGN KEY (nrc) REFERENCES tblSecciones(nrc)) """

        sql_create_table_detalle_secciones_docentes = """ CREATE TABLE IF NOT EXISTS tblDetalle_Secciones_Docentes (
                                docenteDni TEXT NOT NULL,
                                nrc TEXT NOT NULL,
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
