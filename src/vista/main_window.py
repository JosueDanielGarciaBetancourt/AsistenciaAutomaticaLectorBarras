from datetime import datetime
import hashlib
import secrets  # Para generar un salt aleatorio
import binascii
import re
import os
import sys
from PyQt6 import QtWidgets, QtCore, uic, QtGui
from PyQt6.QtCore import Qt
from ui_files.UI_LogIn import UI_LogIn
from ui_files.UI_MainWindow import UI_MainWindow
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QLabel
from src.vista.Window_Utils import MensajesWindow
from src.modelo.Modelos import Docente, Seccion
from src.modelo.ModelosData import DocenteData, SeccionData
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QThread, pyqtSignal
#from pyzbar import pyzbar


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

    def irAcercaDe(self):
        try:
            self.loadGif()
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

                # Se encontró el texto en la columna 0, ahora se cambia el estado de la columna 2
                item_checkbox = self.mainWindow.tablaTomarAsistencia.item(fila, 2)
                if item_checkbox:
                    item_checkbox.setCheckState(Qt.CheckState.Checked)

                # Marcar la hora actual en la fila
                item_hour = self.mainWindow.tablaTomarAsistencia.item(fila, 3)
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
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 2, item)
                    self.mainWindow.tablaTomarAsistencia.resizeColumnsToContents()
                    self.mainWindow.tablaTomarAsistencia.setColumnWidth(2, 100)
                    self.mainWindow.tablaTomarAsistencia.setItem(fila, 3, self.crear_item_no_editable("-"))

                    # centrar los textos de las columnas DNI(0), %Asistencia(2) y Hora(4)

            else:
                mensaje = "Aún no existe sección con el NRC solicitado en la base de datos"
                MensajesWindow.mostrarMensajeRegistroError(mensaje)
                print(mensaje)
        except Exception as ex:
            mensaje = "Ocurrió un error inesperado al intentar configurar la tablaTomarAsistencia"
            print(mensaje)
            print(ex)

    def getCurrentTextCmbBoxAsignatura(self):
        nrc_selected = self.mainWindow.cmbBoxAsignatura.currentText().split(" - ")[0]

        self.comboBoxAsignaturaCurrentNRC = nrc_selected
        self.configTablaTomaAsistencia()

    def configTextCmbBoxAsignatura(self):
        busquedaNRCS = SeccionData()
        nrcs = busquedaNRCS.searchNrcs_by_Docente(self.docente)

        for f_nrc in nrcs:
            curso = busquedaNRCS.searchCurso_by_NRC(f_nrc)
            self.mainWindow.cmbBoxAsignatura.addItem(f_nrc + " - " + curso)

    def seleccionarCursoRapidamente(self, nrc):
        try:
            # Obtener el número de ítems en el ComboBox
            num_items = self.mainWindow.cmbBoxAsignatura.count()

            # Iterar sobre los ítems del ComboBox
            for i in range(num_items):
                # Obtener el texto del ítem actual
                item_text = self.mainWindow.cmbBoxAsignatura.itemText(i)

                # Verificar si el texto del ítem comienza con el valor de nrc
                if item_text.startswith(nrc):
                    # Establecer el índice del ComboBox al ítem que coincide
                    self.mainWindow.cmbBoxAsignatura.setCurrentIndex(i)
                    break
            else:
                # Si no se encontró ningún ítem que comience con nrc
                print(f"No se encontró ningún elemento que comience con '{nrc}' en el ComboBox")

            self.irAsistencia()
        except Exception as ex:
            print("Excepción en seleccionarCursoRapidamente en main_window.py:", ex)

    def configDatosUsuario(self):
        try:
            # Configurar datos de perfil de docente
            self.mainWindow.lblCorreoDocente.setText(self.docente.getUsername())
            self.mainWindow.lblNombreDocente.setText(self.docente.getName())
            self.mainWindow.lblPaisDocente.setText(self.docente.getPais())
            self.mainWindow.lblCiudadDocente.setText(self.docente.getCiudad())

            # Configurar cursos correctos en el stackedWidgetCursos
            if self.docente.getUsername() == "jcamarenaf@continental.edu.pe":
                self.mainWindow.stackedWidgetCursos.setCurrentIndex(0)
            elif self.docente.getUsername() == "mrosales@continental.edu.pe":
                self.mainWindow.stackedWidgetCursos.setCurrentIndex(1)

            # Configurar FotoPerfil docente
            busquedaRutaFoto = DocenteData()
            ruta_foto = busquedaRutaFoto.getDocenteFotoPerfil(self.docente)
            # Verificar si la ruta de la foto es válida
            if not os.path.isfile(ruta_foto):
                raise FileNotFoundError(f"Archivo de foto no encontrado: {ruta_foto}")
            # Cargar la imagen en un QPixmap
            pixmap = QPixmap(ruta_foto)
            self.mainWindow.profeFoto.setPixmap(pixmap)
        except Exception as ex:
            print("Excepción en configDatosUsuario en main_window.py", ex)

    def checkboxClickedChangeState(self, item):
        try:
            if item.column() == 2:
                fila = item.row()
                item_checkbox = self.mainWindow.tablaTomarAsistencia.item(fila, 2)
                item_hour = self.mainWindow.tablaTomarAsistencia.item(fila, 3)
                hora_actual = "-"
                if item_checkbox.checkState() == Qt.CheckState.Checked:
                    hora_actual = datetime.now().strftime("%H:%M:%S")
                item_hour.setText(hora_actual)
        except Exception as ex:
            print("Excepción en checkboxClickedChangeState en main_window.py:", ex)

    def loadGif(self):
        movie = QtGui.QMovie("./ui_files/programador.gif")
        self.mainWindow.gifProgramador.setMovie(movie)
        movie.start()


    def initGUI(self):
        # Configuración de datos según username
        self.configDatosUsuario()

        # Configurar ComboBox
        self.mainWindow.cmbBoxAsignatura.clear()

        # Configurar tablaTomarAsistencia
        self.configTextCmbBoxAsignatura()
        self.getCurrentTextCmbBoxAsignatura()
        self.mainWindow.tablaTomarAsistencia.itemClicked.connect(self.checkboxClickedChangeState)

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
        self.mainWindow.pushButtonAcercaDe.clicked.connect(self.irAcercaDe)
        self.mainWindow.btnProfile.clicked.connect(self.showProfile)
        self.mainWindow.btnCloseProfile.clicked.connect(self.closeProfile)
        self.mainWindow.btnNotification.clicked.connect(self.showNotification)
        self.mainWindow.btnCloseNotification.clicked.connect(self.closeNotification)

        # Selección rápida de cursos mrosales@continental.edu.pe
        self.mainWindow.btnCurso30246.clicked.connect(lambda: self.seleccionarCursoRapidamente("30246"))
        self.mainWindow.btnCurso12344.clicked.connect(lambda: self.seleccionarCursoRapidamente("12344"))
        self.mainWindow.btnCurso12345.clicked.connect(lambda: self.seleccionarCursoRapidamente("12345"))

        # Selección rápida de cursos jcamarenaf@continental.edu.pe
        self.mainWindow.btnCurso22888.clicked.connect(lambda: self.seleccionarCursoRapidamente("22888"))
        self.mainWindow.btnCurso12341.clicked.connect(lambda: self.seleccionarCursoRapidamente("12341"))
        self.mainWindow.btnCurso12342.clicked.connect(lambda: self.seleccionarCursoRapidamente("12342"))
        self.mainWindow.btnCurso12343.clicked.connect(lambda: self.seleccionarCursoRapidamente("12343"))
