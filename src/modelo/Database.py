import os



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
                                docenteContraseña VARCHAR(255) NOT NULL) """
        
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

def eliminarBDExistente(self):
        try:
            os.remove("src/modelo/DB_Asistencias.db")
            print("Base de datos existente eliminada correctamente")
        except FileNotFoundError:
            print("No se encontró la base de datos existente")
        except Exception as ex:
            print("Error al eliminar la base de datos existente:", ex) 