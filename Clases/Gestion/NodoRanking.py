# Clases/Gestion/NodoRanking.py
class NodoRanking:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.anterior = None
        self.siguiente = None
