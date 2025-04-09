# cola.py

class NodoCola:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        return self.frente is None

    def encolar(self, valor):
        nuevo = NodoCola(valor)
        if self.esta_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    def primero(self):
        return self.frente.valor if not self.esta_vacia() else None
