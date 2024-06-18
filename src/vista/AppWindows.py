from datetime import datetime
import sys
from PyQt6.QtWidgets import QApplication
from src.vista.login_window import LogInWindow
from src.vista.main_window import MainWindow

class AsistenciaWindow:
    def __init__(self):
        super().__init__()
        self.app = QApplication(sys.argv)
        self.login = LogInWindow()
        # manda señal de que LoginWindows se finalizó correctamente para iniciar el MainWindows
        self.login.login_successful.connect(self.iniciar_main_window) 
        self.app.exec()

    def iniciar_main_window(self, docente):
        self.main = MainWindow(docente)
        self.main.show()
