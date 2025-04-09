# Clases/Gestion/Ranking.py
from .NodoRanking import NodoRanking

class Ranking:
    def __init__(self):
        self.primero = None

    def insertar_ordenado(self, nombre, puntuacion):
        nuevo = NodoRanking(nombre, puntuacion)
        if not self.primero or puntuacion > self.primero.puntuacion:
            nuevo.siguiente = self.primero
            if self.primero:
                self.primero.anterior = nuevo
            self.primero = nuevo
            return

        actual = self.primero
        while actual.siguiente and actual.siguiente.puntuacion >= puntuacion:
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = nuevo
        actual.siguiente = nuevo
        nuevo.anterior = actual

    def cargar_desde_archivo(self, ruta):
        try:
            with open(ruta, 'r') as f:
                for linea in f:
                    if ':' in linea:
                        nombre, pts = linea.strip().split(':')
                        self.insertar_ordenado(nombre, int(pts))
        except FileNotFoundError:
            pass

    def guardar_en_archivo(self, ruta):
        with open(ruta, 'w') as f:
            actual = self.primero
            while actual:
                f.write(f"{actual.nombre}:{actual.puntuacion}\n")
                actual = actual.siguiente

    def to_string(self):
        resultado = "🏆 CLASIFICACIÓN GENERAL 🏆\n"
        actual = self.primero
        pos = 1
        while actual:
            resultado += f"{pos}. {actual.nombre} → {actual.puntuacion} puntos\n"
            actual = actual.siguiente
            pos += 1
        return resultado
