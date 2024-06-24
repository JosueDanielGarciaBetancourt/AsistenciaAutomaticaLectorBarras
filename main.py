from src.modelo.conexion import Conexion
from src.vista.app import App


if __name__ == "__main__":
    try:
        # Iniciar BD
        conexion = Conexion()

        # Iniciar app
        app = App()
    except Exception as e:
        print("Error inesperado en main.py: ", e)

