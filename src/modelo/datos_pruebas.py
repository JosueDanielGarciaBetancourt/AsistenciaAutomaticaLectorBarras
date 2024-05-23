import sqlite3


def insertar_estudiantes(con):
    estudiantes = [
        {'dni': '77348389', 'nombre': 'CARLOS ENRIQUE ALEJANDRO', 'apellido_paterno': 'PAUCARCHUCO', 'apellido_materno': '', 'correo': '77348389@continental.edu.pe'},
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

    try:
        cur = con.cursor()
        sql_insert = """INSERT INTO tblEstudiantes (estuDni, estuNombre, estuApellidoPaterno, estuApellidoMaterno, estuCorreo) 
                        VALUES (?, ?, ?, ?, ?)"""
        
        for estudiante in estudiantes:
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
