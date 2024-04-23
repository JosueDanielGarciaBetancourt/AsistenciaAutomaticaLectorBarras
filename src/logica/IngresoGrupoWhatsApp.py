import webbrowser


class IngresoGrupoWhastApp:
    @staticmethod
    def ingresarGrupoWhatsApp():
        try:
            webbrowser.open("https://wa.me/943867611")
        except Exception as ex:
            print(ex)
