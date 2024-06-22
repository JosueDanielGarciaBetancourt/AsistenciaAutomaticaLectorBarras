from datetime import datetime
import hashlib
import secrets  # Para generar un salt aleatorio
import binascii
import re
import os
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from ui_files.UI_LogIn import UI_LogIn
from ui_files.UI_MainWindow import UI_MainWindow
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from src.vista.Window_Utils import MensajesWindow
from src.modelo.Modelos import Docente, Seccion
from src.modelo.ModelosData import DocenteData, SeccionData
from src.logica.IngresoGrupoWhatsApp import IngresoGrupoWhastApp


class LogInWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.main = None
        self.logInWindow = UI_LogIn()
        self.logInWindow.setupUi(self)
        self.usernameLoged = ""
        self.passwordLoged = ""
        self.initGUI()
        self.mostrar()

    def mostrar(self):
        self.show()

    def cerrar(self):
        self.close()

    def minimizar(self):
        self.showMinimized()

    def closeLogin(self):
        self.cerrar()
        QApplication.quit()
        print("CERRANDO TODO")

    def limpiarCamposLogin(self):
        self.logInWindow.lineEditUserName.setText("")
        self.logInWindow.lineEditPassword.setText("")
        self.logInWindow.lineEditUserName.setPlaceholderText("Nombre de Usuario/Correo Institucional")
        self.logInWindow.lineEditPassword.setPlaceholderText("Password")

    def validar_username(self, username):
        # Pasar a minúsculas para poder validar si se ingresa username con MAYÚSCULAS
        username_lowerCase = username.lower()
        # Expresión regular para validar el formato del nombre de usuario
        patron = r'^[a-zA-Z0-9_.+-]+@continental\.edu\.pe$'
        return re.match(patron, username_lowerCase, re.IGNORECASE) is not None

    def hash_password(self, password, salt=None):
        if salt is None:
            salt = secrets.token_hex(16)  # Genera un salt aleatorio
        # Combina el salt con la contraseña
        salted_password = salt.encode() + password.encode()
        # Aplica el algoritmo de hash SHA-256
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password, salt

    def verificarLogeo(self):
        try:
            username = (self.logInWindow.lineEditUserName.text()).lower()
            password = self.logInWindow.lineEditPassword.text()

            if len(username) == 0:
                self.logInWindow.lineEditUserName.setFocus()
                MensajesWindow.mostrarMensajeRegistroError("Ingrese nombre de usuario")
                print("Ingrese nombre de usuario")
                return
            if len(password) == 0:
                self.logInWindow.lineEditPassword.setFocus()
                MensajesWindow.mostrarMensajeRegistroError("Ingrese contraseña")
                print("Ingrese contraseña")
                return

            if self.validar_username(username):
                print(f"El nombre de usuario {username} es válido")
                self.logInWindow.lineEditUserName.setText(username)
            else:
                self.logInWindow.lineEditUserName.setFocus()
                MensajesWindow.mostrarMensajeRegistroError("El nombre de usuario no tiene el formato correcto.")
                print("El nombre de usuario no tiene el formato correcto.")
                return

            # Mostrar la contraseña real (solo para propósitos de prueba)
            print("Contraseña:", password)

            """
            # Hashea la contraseña y obtiene el salt
            hashed_password, salt = self.hash_password(password)
    
            # Almacenar el hashed_password y el salt en la BD
    
            # Simplemente imprime para demostración
            print("Contraseña hasheada:", hashed_password)
            print("Salt:", salt)
            """

            docente = Docente(username=username, password=password)
            docenteData = DocenteData()
            docenteEncontrado = docenteData.login(docente)
            if docenteEncontrado:  # Encontró el nombre de usuario del docente
                if docenteEncontrado.getPassword():
                    self.usernameLoged = username
                    self.passwordLoged = password
                    self.ingresarApp(docenteEncontrado)
                else:
                    self.logInWindow.lineEditPassword.setFocus()
                    MensajesWindow.mostrarMensajeRegistroError("Contraseña incorrecta")
                    print("Contraseña incorrecta")
            else:
                MensajesWindow.mostrarMensajeRegistroError("No existe docente con esas credenciales")
                print("No existe docente con esas credenciales")
        except Exception as ex:
            print("Excepción durante la verificacion de login:", ex)

    def ingresarApp(self, docenteEncontrado):
        self.hide()
        self.main = MainWindow(docenteEncontrado)
        MensajesWindow.mostrarMensajeRegistroExito(f"Bienvenido a TRICAPP {docenteEncontrado.getName()}")
        print("Entrando a la APP")

    def whatsappEntry(self):
        print("Entrando a whatsapp")
        IngresoGrupoWhastApp.ingresarGrupoWhatsApp()

    def mostrarContrasena(self, state):
        # Verifica si el estado del checkbox es Qt.Checked (2)
        if state:
            # Si está marcado, muestra la contraseña
            self.logInWindow.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            # Si no está marcado, oculta la contraseña
            self.logInWindow.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def initGUI(self):
        try:
            # Agregar login correcto solo para pruebas
            self.limpiarCamposLogin()
            self.logInWindow.lineEditUserName.setText("jcamarenaf@continental.edu.pe")
            self.logInWindow.lineEditPassword.setText("123")
            self.logInWindow.pushButtonIngresar.clicked.connect(self.verificarLogeo)
            self.logInWindow.pushButtonWhatsApp.clicked.connect(self.whatsappEntry)
            self.logInWindow.pushButtonCloseLogIn.clicked.connect(self.closeLogin)
            self.logInWindow.pushButtonMinimizeLogIn.clicked.connect(self.minimizar)
            self.logInWindow.checkBoxShowPassword.stateChanged.connect(self.mostrarContrasena)
        except Exception as e:
            print(e)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, docenteEncontrado):
        super().__init__()
        self.clickPosition = None
        self.windowRestored = False
        self.mainWindow = UI_MainWindow()
        self.mainWindow.setupUi(self)
        self.paginaActual = 0
        self.docente = docenteEncontrado
        self.comboBoxAsignaturaCurrentNRC = ""
        self.initGUI()
        self.mostrar()

    def mostrar(self):
        self.mainWindow.lblSaludoInicio.setText(f"Hola {self.docente.getName()}")
        self.showMaximized()
        self.irInicio()

    def irInicio(self):
        try:
            self.mainWindow.mainStackedWidget.setCurrentIndex(0)  # 0 - Inicio | 1 - Asistencia | 2 - Reporte
            self.paginaActual = 0
        except Exception as ex:
            print(ex)

    def irAsistencia(self):
        try:
            self.mainWindow.mainStackedWidget.setCurrentIndex(1)  # 0 - Inicio | 1 - Asistencia | 2 - Reporte
            self.paginaActual = 1
        except Exception as ex:
            print(ex)

    def irReporte(self):
        try:
            self.mainWindow.mainStackedWidget.setCurrentIndex(2)  # 0 - Inicio | 1 - Asistencia | 2 - Reporte
            self.paginaActual = 2
        except Exception as ex:
            print(ex)

    def closeMoreMenu(self):
        self.mainWindow.btnShowMoreMenu.show()
        self.mainWindow.centerMenuSubContainer.hide()

    def showMoreMenu(self):
        self.mainWindow.btnShowMoreMenu.hide()
        self.mainWindow.centerMenuSubContainer.show()

    def showProfile(self):
        if self.mainWindow.rightMenuContainer.isHidden():
            self.mainWindow.rightMenuContainer.show()
        else:
            self.closeProfile()

    def closeProfile(self):
        self.mainWindow.rightMenuContainer.hide()

    def showNotification(self):
        if self.mainWindow.popupNotificationSubContainer.isHidden():
            self.mainWindow.popupNotificationSubContainer.show()
        else:
            self.closeNotification()

    def closeNotification(self):
        self.mainWindow.popupNotificationSubContainer.hide()

    def closeApp(self):
        # Definir los valores de los parámetros
        titulo = "Confirmar cierre"
        mensaje = "¿Estás seguro de que deseas cerrar la aplicación?"

        # Llamar a la función con los parámetros
        respuesta = MensajesWindow.mostrarMensajeConfirmacion(titulo, mensaje)

        # Verificar la respuesta del usuario
        if respuesta == "Sí":
            self.close()

    def restoreWindowApp(self):
        if self.isMaximized():
            self.showNormal()  # Normal size
            self.windowRestored = True
        else:
            self.showMaximized()  # Big size
            self.windowRestored = False

    def switchFullScreen(self):
        if self.isFullScreen():
            self.showMaximized()  # Big size
        else:
            self.showFullScreen()  # Full screen

    def minimizeApp(self):
        try:
            self.showMinimized()
        except Exception as ex:
            print(ex)

    def buscar_y_marcar_item(self, texto_busqueda):
        num_filas = self.mainWindow.tablaTomarAsistencia.rowCount()
        DNI_Encontrado = False

        for fila in range(num_filas):
            item = self.mainWindow.tablaTomarAsistencia.item(fila, 0)
            if item and item.text() == texto_busqueda:
                DNI_Encontrado = True

                # Se encontró el texto en la columna 0, ahora se cambia el estado de la columna 3
                item_checkbox = self.mainWindow.tablaTomarAsistencia.item(fila, 3)
                if item_checkbox:
                    item_checkbox.setCheckState(Qt.CheckState.Checked)

                # Marcar la hora actual en la fila
                item_hour = self.mainWindow.tablaTomarAsistencia.item(fila, 4)
                hora_actual = datetime.now().strftime("%H:%M:%S")
                item_hour.setText(hora_actual)

                # Desplazar y enfocar en la fila encontrada
                self.mainWindow.tablaTomarAsistencia.scrollToItem(item, QtWidgets.QAbstractItemView.ScrollHint.PositionAtCenter)
                self.mainWindow.tablaTomarAsistencia.setCurrentCell(fila, 0)
                break  # Terminar el bucle después de encontrar el primer DNI

        self.mainWindow.labelRegistrado.show()

        if DNI_Encontrado:
            self.mainWindow.labelRegistrado.setStyleSheet("""
            color: rgb(46, 255, 60);
            """)
            self.mainWindow.labelRegistrado.setText(f"{texto_busqueda} registrado")
        else:
            self.mainWindow.labelRegistrado.setStyleSheet("""
                        color: rgb(220, 50, 60);
                        """)
            self.mainWindow.labelRegistrado.setText(f"{texto_busqueda} no encontrado")

    def validarTextoAsistenciaPorDNI(self, text):
        # Verificar si todos los caracteres son dígitos y la longitud es 8
        if text.isdigit() and len(text) == 8:
            print(f"El texto {text} es un número de 8 dígitos.")
            self.buscar_y_marcar_item(text)
            self.mainWindow.lineEditDNI.setText("")
        else:
            print(f"El texto {text} no es un número de 8 dígitos.")

    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key.Key_F11:
                self.switchFullScreen()
            elif event.key() == Qt.Key.Key_Return:
                lineEdit = self.mainWindow.lineEditDNI
                if lineEdit.hasFocus():
                    self.validarTextoAsistenciaPorDNI(lineEdit.text())
            else:
                super().keyPressEvent(event)
        except Exception as ex:
            print(ex)

    def mousePressEvent(self, event):
        try:
            # Esto servirá para poder mover la ventana a la posición del cursor
            self.clickPosition = event.globalPos()
        except Exception as ex:
            print(ex)

    def mouseMoveEvent(self, event):
        try:
            if self.windowRestored and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()
        except Exception as ex:
            print(ex)

        # Esto servirá para poder mover la ventana a la posición del cursor
        # self.clickPosition = event.globalPos()
        pass

    def mouseMoveEvent(self, event):
        pass
        """if self.windowRestored and event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()"""

    def crear_item_no_editable(self, texto):
        item = QTableWidgetItem(texto)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        return item

    def configTablaTomaAsistencia(self):
        try:
            # Consultar NRC en la base de datos
            seccion = Seccion(NRC=self.comboBoxAsignaturaCurrentNRC)
            seccionData = SeccionData()
            seccionEncontrada = seccionData.searchSeccion(seccion)

            self.mainWindow.tablaTomarAsistencia.clearContents()
            self.mainWindow.tablaTomarAsistencia.setRowCount(0)

            if seccionEncontrada:  # Encontró el NRC de la sección
                NRC = seccionEncontrada.getNRC()
                # Consultar estudiantes con NRC encontrado
                try:
                    listaObjetosEstudiantes = seccionData.searchEstudiantes_by_NRC(NRC)
                    if listaObjetosEstudiantes is None:
                        raise ValueError("No se encontraron estudiantes para el NRC proporcionado.")
                except Exception as e:
                    print("Error al ejecutar searchEstudiantes_by_NRC:", e)
                    mensaje = "Error al buscar estudiantes por NRC"
                    MensajesWindow.mostrarMensajeRegistroError(mensaje)
                    return

                for estudiante in listaObjetosEstudiantes:
                    fila = self.mainWindow.tablaTomarAsistencia.rowCount()
                    self.mainWindow.tablaTomarAsistencia.insertRow(fila)

                    # Datos del estudiante
                    dni, nombre, ap_paterno, ap_materno, correo = estudiante.getEstudianteAttributes()

                    # Establecer los datos en las celdas de la fila
                    # Hacer no editable las columnas DNI(0), Estudiante(1), Asistencia(2) y Hora(4)
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 0, self.crear_item_no_editable(dni))
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 1, self.crear_item_no_editable(
                        f"{nombre} {ap_paterno} {ap_materno}"))
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 2, self.crear_item_no_editable("0%"))

                    # Insertar checkbox de estado a la columna 3 de la tablaTomarAsistencia encontrada
                    item = QTableWidgetItem()
                    item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                    item.setCheckState(Qt.CheckState.Unchecked)  # Estado inicial: desmarcado
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 3, item)
                    self.mainWindow.tablaTomarAsistencia.resizeColumnsToContents()
                    self.mainWindow.tablaTomarAsistencia.setColumnWidth(3, 100)
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 4, self.crear_item_no_editable("-"))

                    # centrar los textos de las columnas DNI(0), %Asistencia(2) y Hora(4)

            else:
                mensaje = "Aún no existe sección con el NRC solicitado en la base de datos"
                MensajesWindow.mostrarMensajeRegistroError(mensaje)
                print(mensaje)
        except Exception as ex:
            mensaje = "Ocurrió un error inesperado al intentar configurar la tablaTomarAsistencia"
            print(mensaje)
            print(ex)

    def getCurrentTextCmbBoxAsignatura(self, text):
        # Dividir la cadena en partes usando el guion como delimitador
        partes = text.split("-")

        # Seleccionar la parte después del guion (el segundo elemento de la lista resultante)
        nrc = partes[1]

        self.comboBoxAsignaturaCurrentNRC = nrc
        self.configTablaTomaAsistencia()

    def initGUI(self):
        # Iniciar con el curso de Dirección de Proyects (index = 3)
        self.mainWindow.cmbBoxAsignatura.setCurrentIndex(3)

        # Configurar tablaTomarAsistencia
        self.getCurrentTextCmbBoxAsignatura(self.mainWindow.cmbBoxAsignatura.currentText())

        # Ocultar algunos elementos
        self.mainWindow.centerMenuSubContainer.hide()
        self.mainWindow.popupNotificationSubContainer.hide()
        self.mainWindow.labelRegistrado.hide()

        # Obtener el NRC actual del combo box
        self.mainWindow.cmbBoxAsignatura.currentTextChanged.connect(self.getCurrentTextCmbBoxAsignatura)

        # Conectar botones a las distintas acciones
        self.mainWindow.closeBtn.clicked.connect(self.closeApp)
        self.mainWindow.restoreBtn.clicked.connect(self.restoreWindowApp)
        self.mainWindow.minimizeBtn.clicked.connect(self.minimizeApp)
        self.mainWindow.btnCloseMoreMenu.clicked.connect(self.closeMoreMenu)
        self.mainWindow.btnShowMoreMenu.clicked.connect(self.showMoreMenu)
        self.mainWindow.pushButtonInicio.clicked.connect(self.irInicio)
        self.mainWindow.pushButtonAsistencia.clicked.connect(self.irAsistencia)
        self.mainWindow.pushButtonReporte.clicked.connect(self.irReporte)
        self.mainWindow.btnProfile.clicked.connect(self.showProfile)
        self.mainWindow.btnCloseProfile.clicked.connect(self.closeProfile)
        self.mainWindow.btnNotification.clicked.connect(self.showNotification)
        self.mainWindow.btnCloseNotification.clicked.connect(self.closeNotification)


class AsistenciaWindow:
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.login = LogInWindow()
        self.app.exec()
