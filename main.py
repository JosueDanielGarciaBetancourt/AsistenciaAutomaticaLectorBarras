import datetime
from src.vista.Window_Utils import MensajesWindow
from src.vista.AppWindows import AsistenciaWindow
from src.modelo.conexion import Conexion
from src.vista.app import App

datos_personas = {
    "77043114": {"nombre": "Josué", "apellido_paterno": "García", "apellido_materno": "Betancourt",
                 "edad": 22, "sexo": "Masculino"}, 
    "77331712": {"nombre": "Raul", "apellido_paterno": "Torre", "apellido_materno": "Medina",
                 "edad": 21, "sexo": "Masculino"},
    "74465364": {"nombre": "David", "apellido_paterno": "Contreras", "apellido_materno": "Cerrón",
                 "edad": 20, "sexo": "Femenino"},
    "78104318": {"nombre": "Yoni", "apellido_paterno": "Orihuela", "apellido_materno": "Gonzales",
                 "edad": 69, "sexo": "Femenino"},
    "12345678": {"nombre": "María", "apellido_paterno": "Quispe", "apellido_materno": "Mamani",
                 "edad": 30, "sexo": "Femenino"}
}


def buscar_persona_por_dni(dni):
    if dni in datos_personas:
        persona = datos_personas[dni]
        hora_ingreso = datetime.datetime.now().strftime("%H:%M:%S")
        return {
            "nombre": persona["nombre"],
            "apellido_paterno": persona["apellido_paterno"],
            "apellido_materno": persona["apellido_materno"],
            "edad": persona["edad"],
            "sexo": persona["sexo"],
            "hora_ingreso": hora_ingreso
        }
    else:
        return None


def main():
    dni = input("\nIngresar DNI (8 dígitos): ")
    if len(dni) != 8 or not dni.isdigit():
        mensaje = "El DNI ingresado no es válido."
        MensajesWindow.mostrarMensajeRegistroError(mensaje)
        return

    resultado_busqueda = buscar_persona_por_dni(dni)
    if resultado_busqueda:
        print("DATOS DEL ESTUDIANTE")
        print("Nombre:", resultado_busqueda["nombre"])
        print("Ap. Paterno:", resultado_busqueda["apellido_paterno"])
        print("Ap. Materno:", resultado_busqueda["apellido_materno"])
        print("Edad:", resultado_busqueda["edad"])
        print("Sexo:", resultado_busqueda["sexo"])
        print("Hora de ingreso:", resultado_busqueda["hora_ingreso"])
    else:
        mensaje = "El DNI ingresado no fue encontrado en la base de datos."
        MensajesWindow.mostrarMensajeBusquedaError(mensaje)


if __name__ == "__main__":
    try:
        # Iniciar BD
        conexion = Conexion()

        # Iniciar app
        app = App()
    except Exception as e:
        print("Error inesperado en main.py: ", e)

