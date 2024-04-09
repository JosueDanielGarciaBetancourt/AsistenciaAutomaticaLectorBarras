import sqlite3


class Conexion:
    def __init__(self):
        try:
            self.con = sqlite3.connect("src/modelo/AsistenciaAppDB.db")
            print("Creando tablas")
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_create_table1 = """ CREATE TABLE IF NOT EXISTS tblEstudiantes (
                                estDNI TEXT UNIQUE PRIMARY KEY,
                                estNombre TEXT, 
                                estApellidos TEXT) """

        sql_create_table2 = """ CREATE TABLE IF NOT EXISTS tblDocentes (
                                        docDNI TEXT UNIQUE PRIMARY KEY,
                                        docNombre TEXT, 
                                        docApellidos TEXT,
                                        docUsername,
                                        docPassword) """

        sql_create_table3 = """ CREATE TABLE IF NOT EXIST tblCursos (
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
            print("Error al insertar estudiante:", ex)

    def conectar(self):
        return self.con
