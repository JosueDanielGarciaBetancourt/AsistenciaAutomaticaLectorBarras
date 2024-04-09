import hashlib
import secrets  # Para generar un salt aleatorio
import binascii

from PyQt6 import QtWidgets
from ui_files.UI_LogIn import Ui_LogIn
from PyQt6.QtWidgets import QApplication
from src.vista.Window_Utils import MensajesWindow
import re


class LogInWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.logInWindow = Ui_LogIn()
        self.logInWindow.setupUi(self)
        self.initGUI()
        self.mostrar()

    def mostrar(self):
        self.show()

    def cerrar(self):
        self.close()

    def minimizaar(self):
        self.showMinimized()

    def validar_username(self, username):
        # Expresión regular para validar el formato del nombre de usuario
        patron = r'^[a-zA-Z0-9_.+-]+@continental\.edu\.pe$'
        return re.match(patron, username) is not None

    def hash_password(self, password, salt=None):
        if salt is None:
            salt = secrets.token_hex(16)  # Genera un salt aleatorio
        # Combina el salt con la contraseña
        salted_password = salt.encode() + password.encode()
        # Aplica el algoritmo de hash SHA-256
        hashed_password = hashlib.sha256(salted_password).hexdigest()
        return hashed_password, salt

    def ingresarApp(self):
        username = self.logInWindow.lineEditUserName.text()
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
            print("El nombre de usuario es válido.")
        else:
            self.logInWindow.lineEditUserName.setFocus()
            MensajesWindow.mostrarMensajeRegistroError("El nombre de usuario no tiene el formato correcto.")
            print("El nombre de usuario no tiene el formato correcto.")
            return

        # Mostrar la contraseña real (solo para propósitos de prueba)
        print("Contraseña real:", password)

        # Hashea la contraseña y obtiene el salt
        hashed_password, salt = self.hash_password(password)

        # Almacenar el hashed_password y el salt en la BD

        # Simplemente imprime para demostración
        print("Contraseña hasheada:", hashed_password)
        print("Salt:", salt)

        MensajesWindow.mostrarMensajeRegistroExito(username)
        print("Entrando a la APP")

    def wspEntry(self):
        print("Entrando a whatsapp")

    def initGUI(self):
        try:
            self.logInWindow.pushButtonIngresar.clicked.connect(self.ingresarApp)
            self.logInWindow.pushButtonWhatsApp.clicked.connect(self.wspEntry)
            self.logInWindow.pushButtonCloseLogIn.clicked.connect(self.close)
            self.logInWindow.pushButtonMinimizeLogIn.clicked.connect(self.minimizaar)
        except Exception as e:
            print(e)


class AsistenciaWindow:
    def __init__(self):
        super().__init__()
        self.app = QApplication([])
        self.login = LogInWindow()
        self.app.exec()
