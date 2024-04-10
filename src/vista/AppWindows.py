import hashlib
import secrets  # Para generar un salt aleatorio
import binascii
import re
from PyQt6 import QtWidgets
from ui_files.UI_LogIn import UI_LogIn
from ui_files.UI_MainWindow import UI_MainWindow
from PyQt6.QtWidgets import QApplication
from src.vista.Window_Utils import MensajesWindow
from src.modelo.DocenteData import DocenteData
from src.modelo.Docente import Docente


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
        self.logInWindow.lineEditUserName.setText("Nombre de Usuario/Correo Institucional")
        self.logInWindow.lineEditPassword.setText("Password")

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
                    self.ingresarApp()
                else:
                    self.logInWindow.lineEditPassword.setFocus()
                    MensajesWindow.mostrarMensajeRegistroError("Contraseña incorrecta")
                    print("Contraseña incorrecta")
            else:
                MensajesWindow.mostrarMensajeRegistroError("No existe docente con esas credenciales")
                print("No existe docente con esas credenciales")
        except Exception as ex:
            print("Excepción durante la verificacion de login:", ex)

    def ingresarApp(self):
        self.hide()
        self.main = MainWindow()
        MensajesWindow.mostrarMensajeRegistroExito(f"Bienvenido {self.usernameLoged}")
        print("Entrando a la APP")

    def whatsappEntry(self):
        print("Entrando a whatsapp")
        self.limpiarCamposLogin()

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
            # Agregar login correcto para pruebas
            self.logInWindow.lineEditUserName.setText("jcamarenaf@continental.edu.pe")
            self.logInWindow.lineEditPassword.setText("123456")

            self.logInWindow.pushButtonIngresar.clicked.connect(self.verificarLogeo)
            self.logInWindow.pushButtonWhatsApp.clicked.connect(self.whatsappEntry)
            self.logInWindow.pushButtonCloseLogIn.clicked.connect(self.closeLogin)
            self.logInWindow.pushButtonMinimizeLogIn.clicked.connect(self.minimizar)
            self.logInWindow.checkBoxShowPassword.stateChanged.connect(self.mostrarContrasena)
        except Exception as e:
            print(e)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = UI_MainWindow()
        self.mainWindow.setupUi(self)
        self.initGUI()
        self.mostrar()

    def mostrar(self):
        self.showMaximized()

    def cerrar(self):
        self.close()

    def initGUI(self):
        pass

class AsistenciaWindow:
    def __init__(self):
        super().__init__()
        self.app = QApplication([])
        self.login = LogInWindow()
        self.app.exec()
