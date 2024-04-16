import os
import sqlite3


class Conexion:
    def __init__(self):
        try:
            self.con = sqlite3.connect("src/modelo/AsistenciaAppDB.db")
            print("Conexión establecida")
            self.Verdatos()
            if not self.verificarTablasCreadas():
                print("Creando tablas")
                self.crearTablas()
        except Exception as ex:
            print("Excepción en Conexion:", ex)

    def eliminarBDExistente(self):
        try:
            self.con.close()  # Cerrar la conexión antes de eliminar la base de datos
            os.remove("src/modelo/AsistenciaAppDB.db")
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
            sql_insert = """ INSERT INTO tblDocentes (docDNI, docNombre, docApellidos, docUsername, docPassword) VALUES (
                                                     '41280062', 
                                                     'Judith',
                                                     'Camarena Flores',
                                                     'jcamarenaf@continental.edu.pe',
                                                     '123456') """
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
        except sqlite3.IntegrityError:
            print("Ya se creó este docente")
        except Exception as ex:
            print("Error al Insertar Docente:", ex)

    def verificarTablasCreadas(self):
        cursor = self.con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('tblEstudiantes', 'tblDocentes', 'tblCursos')")
        tablas_existentes = [tabla[0] for tabla in cursor.fetchall()]

        if len(tablas_existentes) == 3:
            print("Tablas Existentes Verificadas")
            return True
        else:
            print("Tablas no encontradas ...")
            return False
    
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
        return sqlite3.connect("src/modelo/AsistenciaAppDB.db")
