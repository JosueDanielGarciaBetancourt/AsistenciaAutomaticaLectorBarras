import sqlite3


def insertar_estudiantes(con):
    pass

def insertar_docentes(con):
    try:
        cur = con.cursor()
        sql_insert = """INSERT INTO tblDocentes 
                        (docenteDni, docenteNombre, docenteApellidoPaterno, docenteApellidoMaterno, 
                        docentePais, docenteCiudad, docenteCorreo, docenteContraseña) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        
        docentes = [
            ('41280062', 'Judith', 'Camarena', 'Flores', 'Perú', 'Huancayo', 'jcamarenaf@continental.edu.pe', '123'),
            ('19821000', 'Meliton Julio', 'Rosales', 'Pecho', 'Perú', 'Huancayo', 'mrosales@continental.edu.pe', '123')
        ]
        
        cur.executemany(sql_insert, docentes)
        con.commit()
    except sqlite3.IntegrityError:
        print("Ya se creó este docente")
    except Exception as ex:
        print("Error al insertar docente:", ex)
