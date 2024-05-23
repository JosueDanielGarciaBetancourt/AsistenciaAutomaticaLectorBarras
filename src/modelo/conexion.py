import os
import sqlite3
import src.modelo.database as database
import src.modelo.datos_pruebas as datos_pruebas

class Conexion:
    def __init__(self): #Verificación de la BD tanto en directorio como de tablas.
        try:
            self.rutaActual = os.path.dirname(__file__)
            db_path = os.path.join(self.rutaActual, 'DB_Asistencias.db')

            if not os.path.exists(db_path):
                print("Base de datos no encontrada. Creando nueva base de datos...")
                self.crearBaseDatos()
            else:
                self.con = sqlite3.connect(db_path)
                print("Base de datos encontrada. Verificando tablas...")
                if not self.verificarTablasCreadas():
                    print("Tablas no completas. Eliminando y recreando tablas...")
                    self.crearTablasDB()
                else:
                    print("Tablas existentes verificadas.")
                self.crearDocentes()  #DATOS PARA PRUEBAS (CAMBIAR EN LAS FUTURAS VERSIONES)
                self.crearEstudiantes() #DATOS PARA PRUEBAS (CAMBIAR EN LAS FUTURAS VERSIONES)
                print("Conexión establecida con", self.con)
        except sqlite3.Error as e:
            print("Error al conectar a la base de datos:", e)

    def crearBaseDatos(self):
        database.crear_db_nueva(self.rutaActual)

    def eliminarBDExistente(self):
        database.eliminar_db_existente(self.con, self.rutaActual)

    def verificarTablasCreadas(self):
        return database.verificar_tablas_db(self.con)
        
    def crearTablasDB(self):
        database.crear_tablas(self.con)

    def crearDocentes(self):
        datos_pruebas.insertar_docentes(self.con)

    def crearEstudiantes(self):
        datos_pruebas.insertar_estudiantes(self.con)

    @staticmethod
    def conectar():
        return sqlite3.connect("src/modelo/DB_Asistencias.db")
