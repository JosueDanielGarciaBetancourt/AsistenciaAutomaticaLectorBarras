from datetime import datetime
import hashlib
import secrets  # Para generar un salt aleatorio
import binascii
import re
import os
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt, pyqtSignal
from ui_files.UI_LogIn import UI_LogIn
from ui_files.UI_MainWindow import UI_MainWindow
from PyQt6.QtWidgets import QApplication, QTableWidgetItem
from src.vista.Window_Utils import MensajesWindow
from src.modelo.Modelos import Docente, Seccion
from src.modelo.ModelosData import DocenteData, SeccionData
import webbrowser





class LogInWindow(QtWidgets.QWidget):
    login_successful = pyqtSignal(Docente)  # Señal para indicar login exitoso

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
    
    def verificarInput(self):
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
        except Exception as ex:
            print("Excepción durante la verificacion de login:", ex)

    def verificarLogeo(self):
        self.verificarInput()
        try:
            username = (self.logInWindow.lineEditUserName.text()).lower()
            password = self.logInWindow.lineEditPassword.text()

            docente = Docente(correo=username, password=password)
            docenteData = DocenteData()
            docenteEncontrado = docenteData.getDocenteData(docente)
            if docenteEncontrado:  
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
        self.login_successful.emit(docenteEncontrado)  # Emitir señal de login exitoso
        MensajesWindow.mostrarMensajeRegistroExito(f"Bienvenido a TRICAPP {docenteEncontrado.getName()}")
        print("Entrando a la APP")

    def whatsappEntry(self):
        print("Entrando a whatsapp")
        try:
            webbrowser.open("https://wa.me/933380704")
        except Exception as ex:
            print(ex)

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
            self.logInWindow.lineEditUserName.setText("mrosales@continental.edu.pe")
            self.logInWindow.lineEditPassword.setText("123")
            self.logInWindow.pushButtonIngresar.clicked.connect(self.verificarLogeo)
            self.logInWindow.pushButtonWhatsApp.clicked.connect(self.whatsappEntry)
            self.logInWindow.pushButtonCloseLogIn.clicked.connect(self.closeLogin)
            self.logInWindow.pushButtonMinimizeLogIn.clicked.connect(self.minimizar)
            self.logInWindow.checkBoxShowPassword.stateChanged.connect(self.mostrarContrasena)
        except Exception as e:
            print(e)