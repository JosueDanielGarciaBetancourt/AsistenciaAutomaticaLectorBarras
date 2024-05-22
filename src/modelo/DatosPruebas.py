import sqlite3
import conexion

class DatosPruebas:
    def __init__(self):
         pass
    
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
                sql_insert = """ INSERT INTO tblDocentes 
                (docenteDni, docenteNombre, docenteApellidoPaterno, docenteApellidoMaterno, docenteCorreo, docenteContraseña) 
                VALUES ('41280062', 
                        'Judith',
                        'Camarena',
                        'Flores',
                        'jcamarenaf@continental.edu.pe',
                        '123456') """
                cur = self.con.cursor()
                cur.execute(sql_insert)
                self.con.commit()
            except sqlite3.IntegrityError:
                print("Ya se creó este docente")
            except Exception as ex:
                print("Error al Insertar Docente:", ex)
