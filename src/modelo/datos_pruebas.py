import sqlite3


estudiantes_DP = [
        {'dni': '77348389', 'nombre': 'CARLOS ENRIQUE', 'apellido_paterno': 'ALEJANDRO', 'apellido_materno': 'PAUCARCHUCO', 'correo': '77348389@continental.edu.pe'},
        {'dni': '74651261', 'nombre': 'OLENKA NOELIA', 'apellido_paterno': 'ALMONACID', 'apellido_materno': 'TAPIA', 'correo': '74651261@continental.edu.pe'},
        {'dni': '76418687', 'nombre': 'JACK JEYSON', 'apellido_paterno': 'AUCCATOMA', 'apellido_materno': 'ROJAS', 'correo': '76418687@continental.edu.pe'},
        {'dni': '71257598', 'nombre': 'DERIANN URIEL', 'apellido_paterno': 'BALDEON', 'apellido_materno': 'GUZMAN', 'correo': '71257598@continental.edu.pe'},
        {'dni': '75740805', 'nombre': 'SUGEY YOSELYN', 'apellido_paterno': 'BARZOLA', 'apellido_materno': 'SEGURA', 'correo': '75740805@continental.edu.pe'},
        {'dni': '74286460', 'nombre': 'GEORGE BRANDO', 'apellido_paterno': 'CALDERON', 'apellido_materno': 'LOPEZ', 'correo': '74286460@continental.edu.pe'},
        {'dni': '72868011', 'nombre': 'ZARELY', 'apellido_paterno': 'CANCHANYA', 'apellido_materno': 'QUIÑONEZ', 'correo': '72868011@continental.edu.pe'},
        {'dni': '71624670', 'nombre': 'JORDY STEVE', 'apellido_paterno': 'CHANCASANAMPA', 'apellido_materno': 'TORRES', 'correo': '71624670@continental.edu.pe'},
        {'dni': '76040442', 'nombre': 'LUIS ANGEL', 'apellido_paterno': 'CONDORI', 'apellido_materno': 'RAMON', 'correo': '76040442@continental.edu.pe'},
        {'dni': '74465364', 'nombre': 'DAVID ANTHONY', 'apellido_paterno': 'CONTRERAS', 'apellido_materno': 'CERRON', 'correo': '74465364@continental.edu.pe'},
        {'dni': '75847320', 'nombre': 'SORAYDA MAGDALENA', 'apellido_paterno': 'CRISPIN', 'apellido_materno': 'ZEVALLOS', 'correo': '75847320@continental.edu.pe'},
        {'dni': '75025598', 'nombre': 'DAYANNE GERMAYORI', 'apellido_paterno': 'GARAY', 'apellido_materno': 'CANTA', 'correo': '75025598@continental.edu.pe'},
        {'dni': '77043114', 'nombre': 'JOSUE DANIEL', 'apellido_paterno': 'GARCIA', 'apellido_materno': 'BETANCOURT', 'correo': '77043114@continental.edu.pe'},
        {'dni': '78104318', 'nombre': 'JOHONNY ANTONIO', 'apellido_paterno': 'GONZALES', 'apellido_materno': 'ORIHUELA', 'correo': '78104318@continental.edu.pe'},
        {'dni': '75225970', 'nombre': 'GABRIELA', 'apellido_paterno': 'GUTIERREZ', 'apellido_materno': 'CARNICA', 'correo': '75225970@continental.edu.pe'},
        {'dni': '60906025', 'nombre': 'ELENA', 'apellido_paterno': 'GUTIERREZ', 'apellido_materno': 'CONDORI', 'correo': '60906025@continental.edu.pe'},
        {'dni': '75059693', 'nombre': 'EDWAR PAULINO', 'apellido_paterno': 'GUZMAN', 'apellido_materno': 'HUAMAN', 'correo': '75059693@continental.edu.pe'},
        {'dni': '72847470', 'nombre': 'NICOLAS FISHER', 'apellido_paterno': 'HERMOZA', 'apellido_materno': 'VILLAVICENCIO', 'correo': '72847470@continental.edu.pe'},
        {'dni': '72276440', 'nombre': 'LAURA PATRICIA', 'apellido_paterno': 'HERNANDEZ', 'apellido_materno': 'CALZADA', 'correo': '72276440@continental.edu.pe'},
        {'dni': '70063117', 'nombre': 'HENRRY', 'apellido_paterno': 'HUANCA', 'apellido_materno': 'MENDOZA', 'correo': '70063117@continental.edu.pe'},
        {'dni': '71029235', 'nombre': 'LEZLY JENYFER', 'apellido_paterno': 'JUSTINIANO', 'apellido_materno': 'ESPINOZA', 'correo': '71029235@continental.edu.pe'},
        {'dni': '74974962', 'nombre': 'JOSUE ELI', 'apellido_paterno': 'LORENZO', 'apellido_materno': 'MASGO', 'correo': '74974962@continental.edu.pe'},
        {'dni': '76320956', 'nombre': 'JAIME EDUARDO', 'apellido_paterno': 'MEDINA', 'apellido_materno': 'SOCUALAYA', 'correo': '76320956@continental.edu.pe'},
        {'dni': '72848846', 'nombre': 'ERICK', 'apellido_paterno': 'MELENDEZ', 'apellido_materno': 'VALENZUELA', 'correo': '72848846@continental.edu.pe'},
        {'dni': '75262040', 'nombre': 'FIORELLA JAQUELIN', 'apellido_paterno': 'MENIZ', 'apellido_materno': 'ZEVALLOS', 'correo': '75262040@continental.edu.pe'},
        {'dni': '76048539', 'nombre': 'RAUL ANGEL', 'apellido_paterno': 'POCCOMO', 'apellido_materno': 'ROJAS', 'correo': '76048539@continental.edu.pe'},
        {'dni': '75990434', 'nombre': 'NYKOL KATIA', 'apellido_paterno': 'QUISPE', 'apellido_materno': 'TOMAS', 'correo': '75990434@continental.edu.pe'},
        {'dni': '72687248', 'nombre': 'JEANPIERE OSCAR', 'apellido_paterno': 'RAMOS', 'apellido_materno': 'PATRICIO', 'correo': '72687248@continental.edu.pe'},
        {'dni': '73125046', 'nombre': 'JHENNY LAURA', 'apellido_paterno': 'ROBLES', 'apellido_materno': 'HUAMAN', 'correo': '73125046@continental.edu.pe'},
        {'dni': '73592480', 'nombre': 'ANGELA ESTHER', 'apellido_paterno': 'ROMAN', 'apellido_materno': 'VELIZ', 'correo': '73592480@continental.edu.pe'},
        {'dni': '60829809', 'nombre': 'MARLON ANDRES', 'apellido_paterno': 'SALINAS', 'apellido_materno': 'GAMION', 'correo': '60829809@continental.edu.pe'},
        {'dni': '75174610', 'nombre': 'KELY SAIDA', 'apellido_paterno': 'SEGOVIA', 'apellido_materno': 'LIZARBE', 'correo': '75174610@continental.edu.pe'},
        {'dni': '72868006', 'nombre': 'CLAUDETTE SVIETTA', 'apellido_paterno': 'SERNA', 'apellido_materno': 'BONTEMPS', 'correo': '72868006@continental.edu.pe'},
        {'dni': '77331712', 'nombre': 'RAUL ALEJANDRO', 'apellido_paterno': 'TORRE', 'apellido_materno': 'MEDINA', 'correo': '77331712@continental.edu.pe'},
        {'dni': '72779724', 'nombre': 'GEORGE RUSSELL', 'apellido_paterno': 'TORRES', 'apellido_materno': 'GERONIMO', 'correo': '72779724@continental.edu.pe'},
        {'dni': '70215975', 'nombre': 'MESIAS NICOLAS', 'apellido_paterno': 'URBANO', 'apellido_materno': 'YARINGANO', 'correo': '70215975@continental.edu.pe'},
        {'dni': '74349682', 'nombre': 'FRANK JORDY', 'apellido_paterno': 'VARGAS', 'apellido_materno': 'ROJAS', 'correo': '74349682@continental.edu.pe'},
        {'dni': '72250043', 'nombre': 'JULIO CESAR', 'apellido_paterno': 'VASQUEZ', 'apellido_materno': 'PAQUIYAURI', 'correo': '72250043@continental.edu.pe'},
        {'dni': '73017853', 'nombre': 'JEFFRY JHAIR', 'apellido_paterno': 'VELIZ', 'apellido_materno': 'MARIN', 'correo': '73017853@continental.edu.pe'},
        {'dni': '71211595', 'nombre': 'PILAR', 'apellido_paterno': 'VILLAGARAY', 'apellido_materno': 'ORIHUELA', 'correo': '71211595@continental.edu.pe'},
        {'dni': '73248851', 'nombre': 'MELISA ELVIRA', 'apellido_paterno': 'VILLANUEVA', 'apellido_materno': 'AYUQUE', 'correo': '73248851@continental.edu.pe'},
        {'dni': '72913436', 'nombre': 'SEBASTIAN MATIAS', 'apellido_paterno': 'YARINGAÑO', 'apellido_materno': 'ROMERO', 'correo': '72913436@continental.edu.pe'},
        {'dni': '71864080', 'nombre': 'IRVING JHAIR', 'apellido_paterno': 'YUPANQUI', 'apellido_materno': 'PAQUIYAURI', 'correo': '71864080@continental.edu.pe'}
    ]

estudiantes_IS = [
    {'dni': '73881650', 'nombre': 'CARLOS DANIEL', 'apellido_paterno': 'AGUIRRE', 'apellido_materno': 'SOLIS', 'correo': '73881650@continental.edu.pe'},
    {'dni': '76324510', 'nombre': 'MARICRUZ', 'apellido_paterno': 'ARTICA', 'apellido_materno': 'CASALLO', 'correo': '76324510@continental.edu.pe'},
    {'dni': '71099298', 'nombre': 'JUBALY EMILY', 'apellido_paterno': 'AYLAS', 'apellido_materno': 'AQUINO', 'correo': '71099298@continental.edu.pe'},
    {'dni': '71037976', 'nombre': 'NIELS BINET', 'apellido_paterno': 'AYALA', 'apellido_materno': 'AYLAS', 'correo': '71037976@continental.edu.pe'},
    {'dni': '71896621', 'nombre': 'YUNIOR', 'apellido_paterno': 'CAMARENA', 'apellido_materno': 'SUAREZ', 'correo': '71896621@continental.edu.pe'},
    {'dni': '71245653', 'nombre': 'GUIDO ARMANDO', 'apellido_paterno': 'BARRETO', 'apellido_materno': 'POVES', 'correo': '71245653@continental.edu.pe'},
    {'dni': '73041644', 'nombre': 'ADIEL ALESSANDRO', 'apellido_paterno': 'CAPARACHIN', 'apellido_materno': 'MONTES', 'correo': '73041644@continental.edu.pe'},
    {'dni': '75756546', 'nombre': 'CRISTIAN', 'apellido_paterno': 'CCAPA', 'apellido_materno': 'CAPANI', 'correo': '75756546@continental.edu.pe'},
    {'dni': '76038672', 'nombre': 'LETICIA RAQUEL', 'apellido_paterno': 'ESPAÑA', 'apellido_materno': 'SALINAS', 'correo': '76038672@continental.edu.pe'},
    {'dni': '76370944', 'nombre': 'SAMANTHA VANESA', 'apellido_paterno': 'FALCONI', 'apellido_materno': 'NUÑEZ', 'correo': '76370944@continental.edu.pe'},
    {'dni': '72798350', 'nombre': 'JULHINO', 'apellido_paterno': 'HUINCHO', 'apellido_materno': 'CAHUANA', 'correo': '72798350@continental.edu.pe'},
    {'dni': '72458313', 'nombre': 'ALEXANDRA JAZMIN', 'apellido_paterno': 'IVALA', 'apellido_materno': 'CARHUANCHO', 'correo': '72458313@continental.edu.pe'},
    {'dni': '75193764', 'nombre': 'SUSAN NAHOMY', 'apellido_paterno': 'JÁUREGUI', 'apellido_materno': 'ESPINOZA', 'correo': '75193764@continental.edu.pe'},
    {'dni': '70921932', 'nombre': 'KATHERINE', 'apellido_paterno': 'LLANCARI', 'apellido_materno': 'BUJAICO', 'correo': '70921932@continental.edu.pe'},
    {'dni': '74532558', 'nombre': 'ANDREA MILAGROS', 'apellido_paterno': 'LLANOS', 'apellido_materno': 'QUISPE', 'correo': '74532558@continental.edu.pe'},
    {'dni': '74363667', 'nombre': 'MARIA CELESTE', 'apellido_paterno': 'LOPEZ', 'apellido_materno': 'CCACCRO', 'correo': '74363667@continental.edu.pe'},
    {'dni': '81117052', 'nombre': 'VANNYA PALOMA', 'apellido_paterno': 'LOPEZ', 'apellido_materno': 'TANTAVILCA', 'correo': '81117052@continental.edu.pe'},
    {'dni': '70867819', 'nombre': 'JUAN ELIAS', 'apellido_paterno': 'MALLMA', 'apellido_materno': 'QUISPE', 'correo': '70867819@continental.edu.pe'},
    {'dni': '73610089', 'nombre': 'JEFERSON RYDER', 'apellido_paterno': 'MARTINEZ', 'apellido_materno': 'GOMEZ', 'correo': '73610089@continental.edu.pe'},
    {'dni': '74969709', 'nombre': 'FLOR JEMINA', 'apellido_paterno': 'MELCHOR', 'apellido_materno': 'VILLA', 'correo': '74969709@continental.edu.pe'},
    {'dni': '73870854', 'nombre': 'INDIRA PAOLA', 'apellido_paterno': 'PALOMINO', 'apellido_materno': 'CAMPOS', 'correo': '73870854@continental.edu.pe'},
    {'dni': '76304403', 'nombre': 'ABDEL HARUKO', 'apellido_paterno': 'NAKAMURA', 'apellido_materno': 'MOYA', 'correo': '76304403@continental.edu.pe'},
    {'dni': '70238629', 'nombre': 'ANDY JOHAN', 'apellido_paterno': 'RIVAS', 'apellido_materno': 'OSEJO', 'correo': '70238629@continental.edu.pe'},
    {'dni': '70865667', 'nombre': 'SHAYD ALBIERY', 'apellido_paterno': 'QUILCA', 'apellido_materno': 'OLIVERA', 'correo': '70865667@continental.edu.pe'},
    {'dni': '71817092', 'nombre': 'RONALDO SHANDE', 'apellido_paterno': 'RIVERA', 'apellido_materno': 'SIMEON', 'correo': '71817092@continental.edu.pe'},
    {'dni': '75221146', 'nombre': 'MARCOS RENE', 'apellido_paterno': 'RODRIGUEZ', 'apellido_materno': 'PAUCAR', 'correo': '75221146@continental.edu.pe'},
    {'dni': '71277369', 'nombre': 'NAYLA', 'apellido_paterno': 'ROJAS', 'apellido_materno': 'GALLEGOS', 'correo': '71277369@continental.edu.pe'},
    {'dni': '72666523', 'nombre': 'ALEJANDRO FABRIZIO', 'apellido_paterno': 'SALGUERAN', 'apellido_materno': 'PORRAS', 'correo': '72666523@continental.edu.pe'},
    {'dni': '73666565', 'nombre': 'MAURO FABIAN', 'apellido_paterno': 'SINCHE', 'apellido_materno': 'MOLINA', 'correo': '73666565@continental.edu.pe'},
    {'dni': '77331712', 'nombre': 'RAUL ALEJANDRO', 'apellido_paterno': 'TORRE', 'apellido_materno': 'MEDINA', 'correo': '77331712@continental.edu.pe'},
    {'dni': '75838493', 'nombre': 'JOSE MANUEL', 'apellido_paterno': 'SULLCA', 'apellido_materno': 'ARONE', 'correo': '75838493@continental.edu.pe'},
    {'dni': '72870880', 'nombre': 'JHORDAN KEITH', 'apellido_paterno': 'VELASQUEZ', 'apellido_materno': 'KNUTZEN', 'correo': '72870880@continental.edu.pe'},
    {'dni': '72851787', 'nombre': 'RENATO SEBASTIAN', 'apellido_paterno': 'VELIZ', 'apellido_materno': 'VELASQUEZ', 'correo': '72851787@continental.edu.pe'},
    {'dni': '75863060', 'nombre': 'MARYORIE GABRIELA', 'apellido_paterno': 'VERA', 'apellido_materno': 'MUÑOZ', 'correo': '75863060@continental.edu.pe'},
    {'dni': '72763584', 'nombre': 'JAIRO RONALD', 'apellido_paterno': 'YARASCA', 'apellido_materno': 'BATALLA', 'correo': '72763584@continental.edu.pe'},
    {'dni': '71853995', 'nombre': 'ESTEFANY MAYUMI', 'apellido_paterno': 'MUÑICO', 'apellido_materno': 'SOTO', 'correo': '71853995@continental.edu.pe'},
    {'dni': '73975773', 'nombre': 'DANIEL EDGARDO', 'apellido_paterno': 'GIRALDEZ', 'apellido_materno': 'VIVAR', 'correo': '73975773@continental.edu.pe'},
    {'dni': '76279987', 'nombre': 'JHANET MAYORY', 'apellido_paterno': 'HINOSTROZA', 'apellido_materno': 'MELENDEZ', 'correo': '76279987@continental.edu.pe'}
]

estudiantes_TEST = [
    {'dni': '12345601', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345602', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345603', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345604', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345605', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345606', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345607', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345608', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345609', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345610', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345611', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345612', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345613', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345614', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345615', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345616', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345617', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345618', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
    {'dni': '12345619', 'nombre': 'NOMBRE', 'apellido_paterno': 'APELLIDOP', 'apellido_materno': 'APELLIDOM', 'correo': '12345678@continental.edu.pe'},
]


# Verificar si una tabla está vacía antes de insertar datos
def tabla_vacia(con, tabla):
    try:
        cur = con.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {tabla}")
        count = cur.fetchone()[0]
        return count == 0
    except Exception as e:
        print(f"Error al verificar si la tabla {tabla} está vacía:", e)
        return False

def estudiante_existe(con, dni):
    try:
        cur = con.cursor()
        cur.execute("SELECT 1 FROM tblEstudiantes WHERE estuDni = ?", (dni,))
        return cur.fetchone() is not None
    except Exception as e:
        print(f"Error al verificar si el estudiante existe:", e)
        return False

def insertar_estudiantes(con):
    if tabla_vacia(con, 'tblEstudiantes'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblEstudiantes (estuDni, estuNombre, estuApellidoPaterno, estuApellidoMaterno, estuCorreo) 
                            VALUES (?, ?, ?, ?, ?)"""
            
            for estudiante in estudiantes_DP + estudiantes_IS + estudiantes_TEST:
                if not estudiante_existe(con, estudiante['dni']):
                    cur.execute(sql_insert, (
                        estudiante['dni'], 
                        estudiante['nombre'], 
                        estudiante['apellido_paterno'], 
                        estudiante['apellido_materno'], 
                        estudiante['correo']
                    ))
            
            con.commit()
            print("Estudiantes insertados correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar estudiante:", e)
        except Exception as ex:
            print("Error al insertar estudiante:", ex)
    else:
        print("La tabla tblEstudiantes ya tiene datos")


def insertar_docentes(con):
    if tabla_vacia(con, 'tblDocentes'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblDocentes 
                            (docenteDni, docenteNombre, docenteApellidoPaterno, docenteApellidoMaterno, 
                            docentePais, docenteCiudad, docenteCorreo, docenteContraseña, docenteFotoPerfil) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            
            docentes = [
                ('41280062', 'Judith', 'Camarena', 'Flores', 'Perú', 'Huancayo', 'jcamarenaf@continental.edu.pe', '123', './ui_files/fotoIngJudithRounded.png'),
                ('19821000', 'Meliton Julio', 'Rosales', 'Pecho', 'Perú', 'Huancayo', 'mrosales@continental.edu.pe', '123','./ui_files/fotoIngMelitonRounded.png')
            ]
            
            cur.executemany(sql_insert, docentes)
            con.commit()
            print("Docentes insertados correctamente")
        except sqlite3.IntegrityError:
            print("Ya se creó este docente")
        except Exception as ex:
            print("Error al insertar docente:", ex)
    else:
        print("La tabla tblDocentes ya tiene datos")


def insertar_aulas(con):
    if tabla_vacia(con, 'tblAulas'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblAulas (aulaId, aulaPabellon, aulaSalon, aulaCapacidad) VALUES (?, ?, ?, ?)"""
            
            aulas = [
                ('E202', 'E', '202', 50),
                ('C401', 'C', '401', 50),
                ('H704', 'H', '704', 40)
            ]
            
            cur.executemany(sql_insert, aulas)
            con.commit()
            print("Aulas insertadas correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar aulas:", e)
        except Exception as ex:
            print("Error al insertar aulas:", ex)
    else:
        print("La tabla tblAulas ya tiene datos")


def insertar_cursos(con):
    if tabla_vacia(con, 'tblCursos'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblCursos (cursoId, cursoNombre, cursoCredito) VALUES (?, ?, ?)"""
            
            cursos = [
                ('ASUC01365', 'INNOVACIÓN SOCIAL', 2),
                ('ASUC01235', 'DIRECCIÓN DE PROYECTOS', 4),
                ('ASUC01231', 'ASIGNATURA 1 / TEST ', 5),
                ('ASUC01232', 'ASIGNATURA 2 / TEST ', 5),
                ('ASUC01233', 'ASIGNATURA 3 / TEST ', 5)
            ]
            
            cur.executemany(sql_insert, cursos)
            con.commit()
            print("Cursos insertados correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar cursos:", e)
        except Exception as ex:
            print("Error al insertar cursos:", ex)
    else:
        print("La tabla tblCursos ya tiene datos")


def insertar_secciones(con):
    if tabla_vacia(con, 'tblSecciones'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblSecciones (nrc, seccionPeriodo, cursoId) VALUES (?, ?, ?)"""
            
            secciones = [
                ('30246', '202410', 'ASUC01365'),
                ('22888', '202410', 'ASUC01235'),
                ('12341', '202410', 'ASUC01231'),
                ('12342', '202410', 'ASUC01232'),
                ('12343', '202410', 'ASUC01233')
            ]
            
            cur.executemany(sql_insert, secciones)
            con.commit()
            print("Secciones insertadas correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar secciones:", e)
        except Exception as ex:
            print("Error al insertar secciones:", ex)
    else:
        print("La tabla tblSecciones ya tiene datos")


def insertar_detalles_estudiantes_secciones(con):
    if tabla_vacia(con, 'tblDetalle_Estudiantes_Secciones'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblDetalle_Estudiantes_Secciones 
                            (estuDni, nrc, det_estu_seccion_estadoAsistencia, 
                            det_estu_seccion_fechaAsistencia, det_estu_seccion_horaAsistencia) 
                            VALUES (?, ?, ?, ?, ?)"""
            
            detalles_estudiantes = []
            for estudiante in estudiantes_DP:
                detalles_estudiantes.append((
                    estudiante['dni'],
                    '22888',  # NRC de DIRECCIÓN DE PROYECTOS
                    0,  # estadoAsistencia sin registrar
                    '2000-01-01',  # Fecha genérica
                    '00:00:00'  # Hora genérica
                ))
            
            for estudiante in estudiantes_IS:
                detalles_estudiantes.append((
                    estudiante['dni'],
                    '30246',  # NRC de INNOVACIÓN SOCIAL
                    0,  # estadoAsistencia sin registrar
                    '2000-01-01',  # Fecha genérica
                    '00:00:00'  # Hora genérica
                ))

            for estudiante in estudiantes_TEST:
                detalles_estudiantes.append((
                    estudiante['dni'],
                    '12341',  # NRC 
                    0,  # estadoAsistencia sin registrar
                    '2000-01-01',  # Fecha genérica
                    '00:00:00'  # Hora genérica
                ))

                detalles_estudiantes.append((
                    estudiante['dni'],
                    '12342',  # NRC 
                    0,  # estadoAsistencia sin registrar
                    '2000-01-01',  # Fecha genérica
                    '00:00:00'  # Hora genérica
                ))

                detalles_estudiantes.append((
                    estudiante['dni'],
                    '12343',  # NRC 
                    0,  # estadoAsistencia sin registrar
                    '2000-01-01',  # Fecha genérica
                    '00:00:00'  # Hora genérica
                ))
            
            cur.executemany(sql_insert, detalles_estudiantes)
            con.commit()
            print("Detalles de estudiantes en secciones insertados correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar detalles de estudiantes en secciones:", e)
        except Exception as ex:
            print("Error al insertar detalles de estudiantes en secciones:", ex)
    else:
        print("La tabla tblDetalle_Estudiantes_Secciones ya tiene datos")


def insertar_detalles_secciones_aulas(con):
    if tabla_vacia(con, 'tblDetalle_Secciones_Aulas'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblDetalle_Secciones_Aulas 
                            (nrc, aulaId, det_seccion_aula_horaInicio
                            , det_seccion_aula_horaFin, det_seccion_aula_diaSemana) 
                            VALUES (?, ?, ?, ?, ?)"""
            
            detalles_aulas = [
                ('22888', 'E202', '14:00', '17:09', 'Martes'),
                ('30246', 'H704', '10:20', '11:49', 'Viernes'),
                ('22888', 'C401', '14:00', '15:29', 'Miercoles')
            ]
            
            cur.executemany(sql_insert, detalles_aulas)
            con.commit()
            print("Detalles de secciones en aulas insertados correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar detalles de secciones en aulas:", e)
        except Exception as ex:
            print("Error al insertar detalles de secciones en aulas:", ex)
    else:
        print("La tabla tblDetalle_Secciones_Aulas ya tiene datos")


def insertar_detalles_secciones_docentes(con):
    if tabla_vacia(con, 'tblDetalle_Secciones_Docentes'):
        try:
            cur = con.cursor()
            sql_insert = """INSERT INTO tblDetalle_Secciones_Docentes 
                            (nrc, docenteDni) 
                            VALUES (?, ?)"""
            
            detalles_docentes = [
                ('22888', '41280062'),
                ('12341', '41280062'),
                ('12342', '41280062'),
                ('12343', '41280062'),  # DIRECCIÓN DE PROYECTOS con Judith Camarena Flores
                ('30246', '19821000')  # INNOVACIÓN SOCIAL con Meliton Julio Rosales Pecho
            ]
            
            cur.executemany(sql_insert, detalles_docentes)
            con.commit()
            print("Detalles de secciones en docentes insertados correctamente")
        except sqlite3.IntegrityError as e:
            print("Error de integridad al insertar detalles de secciones en docentes:", e)
        except Exception as ex:
            print("Error al insertar detalles de secciones en docentes:", ex)
    else:
        print("La tabla tblDetalle_Secciones_Docentes ya tiene datos")


