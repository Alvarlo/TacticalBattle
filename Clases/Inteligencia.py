from .Personaje import Personaje;

class Inteligencia(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self):
        print("Busca enemigos en 2x2 y revela su ubicacion")