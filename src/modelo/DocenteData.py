import conexion as con
from src.modelo import Docente


class DocenteData:
    def __init__(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()

    def login(self, docente: Docente):
        print(docente)
