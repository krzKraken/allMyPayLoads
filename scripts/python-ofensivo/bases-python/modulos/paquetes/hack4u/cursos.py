class Cursos:
    def __init__(self, nombre, duracion, link):
        self.nombre = nombre
        self.duracion = duracion
        self.link = link

    def __repr__(self) -> str:
        return f"{self.nombre} [{self.duracion} horas ] ({self.link})"


cursos = [
    Cursos("hacking web", 3, "www.hack4u.io/hacking-web"),
    Cursos("hacking mobil", 3, "www.hack4u.io/hacking-mobile"),
    Cursos("hacking apps", 3, "www.hack4u.io/hacking-apps"),
]


def list_cursos():
    for i in cursos:
        print(i)
