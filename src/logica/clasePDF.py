import os
import subprocess
import platform
from datetime import datetime
from PyQt6.QtCore import Qt
from fpdf import FPDF
from src.vista.Window_Utils import MensajesWindow


class GeneradorReporteAsistencia(FPDF):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
        self.generar_reporte_asistencia()

    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Reporte de Asistencia', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def generar_nombre_reporte(self):
        # Obtener la fecha actual
        fecha_actual = datetime.now().strftime('%Y%m%d')

        nrc_curso = self.mainWindow.cmbBoxAsignatura.currentText()
        nrc = nrc_curso.split(" - ")[0]
        nombre_curso = nrc_curso.split(" - ")[1]

        # Crear el directorio si no existe
        if not os.path.exists("PDFs"):
            os.mkdir("PDFs")

        # Generar nombre base del archivo
        base_nombre_archivo = f"Asistencia_{fecha_actual}_{nrc}_{nombre_curso}"

        # Buscar archivos existentes que coincidan con el patrón base
        archivos_existentes = [f for f in os.listdir("PDFs") if f.startswith(base_nombre_archivo) and f.endswith(".pdf")]

        # Determinar el número correlativo
        numero = len(archivos_existentes) + 1

        # Crear nombre del archivo con número correlativo
        nombre_archivo = f"{base_nombre_archivo}_{numero:03d}.pdf"
        self.file_path = os.path.join("PDFs", nombre_archivo)

    def generar_reporte_asistencia(self):
        self.generar_nombre_reporte()

        # Agregar detalles al reporte
        self.add_page()
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Curso: {self.mainWindow.cmbBoxAsignatura.currentText()}', 0, 1)

        # Encabezados de la tabla
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 220, 255)
        self.cell(30, 10, 'DNI', 1, 0, 'C', 1)
        self.cell(80, 10, 'Nombre', 1, 0, 'C', 1)
        self.cell(40, 10, 'Asistencia', 1, 0, 'C', 1)
        self.cell(40, 10, 'Hora', 1, 1, 'C', 1)

        # Contenido de la tabla
        self.set_font('Arial', '', 10)
        num_filas = self.mainWindow.tablaTomarAsistencia.rowCount()
        for fila in range(num_filas):
            dni = self.mainWindow.tablaTomarAsistencia.item(fila, 0).text()
            nombre = self.mainWindow.tablaTomarAsistencia.item(fila, 1).text()
            asistencia = self.mainWindow.tablaTomarAsistencia.item(fila, 2).checkState()
            hora = self.mainWindow.tablaTomarAsistencia.item(fila, 3).text()

            asistencia_texto = "Asistió" if asistencia == Qt.CheckState.Checked else "No asistió"

            self.cell(30, 10, dni, 1)
            self.cell(80, 10, nombre, 1)
            self.cell(40, 10, asistencia_texto, 1)
            self.cell(40, 10, hora, 1, 1)

        # Guardar el PDF en un archivo
        self.output(self.file_path)

        # Mostrar mensaje de éxito
        print("Reporte generado exitosamente.")

    def abrir_reporte(self):
        try:
            if platform.system() == "Windows":
                subprocess.run(["start", "", self.file_path], shell=True, check=True)
            elif platform.system() == "Darwin":  # macOS
                subprocess.run(["open", self.file_path], check=True)
            else:  # Linux y otros sistemas Unix
                subprocess.run(["xdg-open", self.file_path], check=True)
        except Exception as e:
            print("Error al abrir el archivo PDF:", e)
            # Aquí puedes llamar a tu método para mostrar el mensaje de error inesperado
            MensajesWindow.mostrarMensajeErrorInesperado("Error al abrir el reporte de asistencia.")


