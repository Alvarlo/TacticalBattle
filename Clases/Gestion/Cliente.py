
class Cliente:
    def __init__(self, nombre, socket):
        self.nombre = nombre
        self.socket = socket
        self.jugador = None  # se asignará en la partida