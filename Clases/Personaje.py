from abc import ABC, abstractmethod

from abc import ABC

class Personaje(ABC):
    def __init__(self, vida_maxima, vida_actual, danyo, posicion, enfriamiento_restante, equipo, icono):
        self._vida_maxima = vida_maxima
        self._vida_actual = vida_actual
        self._danyo = danyo
        self._posicion = posicion
        self._enfriamiento_restante = enfriamiento_restante
        self._equipo = equipo
        self._icono = icono

    # vida_maxima
    @property
    def vida_maxima(self):
        return self._vida_maxima

    @vida_maxima.setter
    def vida_maxima(self, value):
        self._vida_maxima = value

    # vida_actual
    @property
    def vida_actual(self):
        return self._vida_actual

    @vida_actual.setter
    def vida_actual(self, value):
        self._vida_actual = value

    # danyo
    @property
    def danyo(self):
        return self._danyo

    @danyo.setter
    def danyo(self, value):
        self._danyo = value

    # posicion
    def set_posicion(self,x,y):
        self.posicion = {"x": x, "y": y}

   

    # enfriamiento_restante
    @property
    def enfriamiento_restante(self):
        return self._enfriamiento_restante

    @enfriamiento_restante.setter
    def enfriamiento_restante(self, value):
        self._enfriamiento_restante = value

    # equipo
    @property
    def equipo(self):
        return self._equipo

    @equipo.setter
    def equipo(self, value):
        self._equipo = value

    # icono
    @property
    def icono(self):
        return self._icono

    @icono.setter
    def icono(self, value):
        self._icono = value




    def mover(self,coordenadas,tablero):

        # Convierte la letra en columna (A=0, B=1, C=2, ...)
        letra = coordenadas[0].upper()
        columna = ord(letra) - ord('A')

        # Convierte el número en fila (1=0, 2=1, 3=2, ...)
        fila = int(coordenadas[1:]) - 1

        if tablero.esPosibleMoverAqui(fila,columna):

            # 1. Obtener la posición actual
            actual_x = self.posicion["x"]
            actual_y = self.posicion["y"]

            # 2. Vaciar la celda anterior
            tablero.tablero[actual_x][actual_y] = None

            # 3. Colocar la unidad en la nueva posición
            tablero.colocarUnidad(self, fila, columna)

            # 4. Actualizar la posición de la unidad
            self.set_posicion(fila,columna)

            return True

        else:
            return False
            

    
    @abstractmethod
    def habilidad(self):
        pass
