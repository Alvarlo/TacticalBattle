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
    @property
    def posicion(self):
        return self._posicion

    @posicion.setter
    def posicion(self, value):
        self._posicion = value

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




    @abstractmethod
    def habilidad(self):
        pass
