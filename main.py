from src.vista.AppWindows import AsistenciaWindow
from src.modelo.conexion import Conexion


if __name__ == "__main__":
    try:
        # Iniciar BD
        conexion = Conexion()
        # Iniciar app
        initApp = AsistenciaWindow()
    except Exception as e:
        print("Error inesperado en main.py: ", e)

