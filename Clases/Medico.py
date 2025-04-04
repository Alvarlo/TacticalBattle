from .Personaje import Personaje;

class Medico(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self):
        print("Cura unidad aliada (no militar) con la vida al maximo")