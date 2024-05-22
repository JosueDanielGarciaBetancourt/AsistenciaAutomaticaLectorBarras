from PyQt6 import QtWidgets,  QtGui
from PyQt6.QtWidgets import QMessageBox
import ui_files.resourcesFile


class MensajesWindow:
    # Estilo fijo para los QMessageBox
    estilos = """
       QMessageBox {
           background-color: #2d2d2d;
           font-size: 14px;
           color: #ffffff;
       }
       QMessageBox QLabel {
           color: #ffffff;
       }
       QMessageBox QPushButton {
           background-color: #4a4a4a;
           color: #e6e6e6;
           border: 1px solid #666666;
           border-radius: 5px;
           padding: 6px 12px;
       }
       QMessageBox QPushButton:hover {
           background-color: #5a5a5a;
           border: 1px solid #808080;
       }
       QMessageBox QPushButton:pressed {
           background-color: #3a3a3a;
           border: 1px solid #666666;
       }
       QMessageBox QPushButton:focus {
           outline: none;
           background-color: #4c84ff;
           color: #ffffff;
           border: 1px solid #3367d6;
       }
    """

    @staticmethod
    def mostrarMensaje(titulo, mensaje, icono):
        msgBox = QMessageBox()
        msgBox.setIcon(icono)
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensaje)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        msgBox.setStyleSheet(MensajesWindow.estilos)
        msgBox.setWindowIcon(QtGui.QIcon(":icons/AppIcon.ico"))
        msgBox.exec()

    @staticmethod
    def mostrarMensajeConfirmacion(titulo, mensaje):
        confirmBox = QMessageBox()
        confirmBox.setIcon(QMessageBox.Icon.Question)
        confirmBox.setWindowTitle(titulo)
        confirmBox.setText(mensaje)
        confirmBox.addButton("Sí", QtWidgets.QMessageBox.ButtonRole.YesRole)
        confirmBox.addButton("No", QtWidgets.QMessageBox.ButtonRole.NoRole)
        confirmBox.setStyleSheet(MensajesWindow.estilos)
        confirmBox.setWindowIcon(QtGui.QIcon(":icons/AppIcon.ico"))
        confirmBox.exec()
        return confirmBox.clickedButton().text()

    @staticmethod
    def mostrarMensajeRegistroExito(mensaje):
        MensajesWindow.mostrarMensaje("Registro exitoso", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeRegistroError(mensaje):
        MensajesWindow.mostrarMensaje("Registro fallido", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeBusquedaExito(mensaje):
        MensajesWindow.mostrarMensaje("Búsqueda exitosa", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeBusquedaError(mensaje):
        MensajesWindow.mostrarMensaje("Error en la búsqueda", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeEliminarExito(mensaje):
        MensajesWindow.mostrarMensaje("Éxito al borrar", mensaje, QMessageBox.Icon.Information)

    @staticmethod
    def mostrarMensajeEliminarError(mensaje):
        MensajesWindow.mostrarMensaje("Error al borrar", mensaje, QMessageBox.Icon.Warning)

    @staticmethod
    def mostrarMensajeErrorInesperado(mensaje):
        MensajesWindow.mostrarMensaje("Error inesperado", mensaje, QMessageBox.Icon.Critical)

# Ejemplo de cómo usar la clase con estilos aplicados
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    MensajesWindow.mostrarMensajeRegistroExito("¡Tu registro ha sido exitoso!")
    MensajesWindow.mostrarMensajeRegistroError("Hubo un error en el registro.")
    titulo = "Confirmar cierre"
    mensaje = "¿Estás seguro de que deseas cerrar la aplicación?"
    MensajesWindow.mostrarMensajeConfirmacion(titulo, mensaje)
    app.exec()

