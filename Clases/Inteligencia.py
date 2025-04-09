from .Personaje import Personaje;

class Inteligencia(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self,tablero):
        print("Revelar enemigos en un area de 2x2.")

        while True:
            coordenada = input("Indica la coordenada que quieres atacar o escribe 'volver': ").upper()

            if coordenada == "VOLVER":
                print("Cancelando habilidad de Inteligencia.")
                return

            if len(coordenada) < 2 or not coordenada[1:].isdigit():
                print("Coordenada inválida.")
                continue

            fila = int(coordenada[1:]) - 1
            columna = ord(coordenada[0]) - ord('A')

            # Validación de límites del tablero
            if not (0 <= fila < tablero.cantidadFilas and 0 <= columna < tablero.cantidadColumnas):
                print("Esa coordenada está fuera del tablero.")
                continue

            self.enfriamiento_restante = 2

            return "I"+coordenada
