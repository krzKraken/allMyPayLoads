""" Clase nota """

#!/usr/bin/enb python3


class Nota:
    """Class nota"""

    def __init__(self, contenido):
        self.contenido = contenido

    def __str__(self):
        return f"[gray]{self.contenido}[/gray]"

    def __repr__(self):
        return self.__str__()
