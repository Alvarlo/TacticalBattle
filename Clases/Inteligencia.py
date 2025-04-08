from .Personaje import Personaje;

class Inteligencia(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self,tablero):
        tablero.situacionDelTablero()
        print("Revela enemigos en un área 2x2.")

        while True:
            coordenada = input("Indica la coordenada de la esquina superior izquierda en la que explorar (área 2x2) o escribe 'volver': ").upper()

            if coordenada == "VOLVER":
                print("Cancelando habilidad de Inteligencia.")
                return

            if len(coordenada) < 2 or not coordenada[1:].isdigit():
                print("Coordenada inválida.")
                continue

            fila = int(coordenada[1:]) - 1
            columna = ord(coordenada[0]) - ord('A')

            if fila < 0 or columna < 0 or fila + 1 >= tablero.cantidadFilas or columna + 1 >= tablero.cantidadColumnas:
                print("El área 2x2 se sale del tablero.")
                continue

            enemigos_detectados = []
            for dx in range(2):
                for dy in range(2):
                    objetivo = tablero.tablero[fila + dx][columna + dy]
                    if objetivo is not None:
                        coord = f"{chr(ord('A') + columna + dy)}{fila + dx + 1}"
                        enemigos_detectados.append(f"Detectado: {objetivo.__class__.__name__} en {coord} con {objetivo.vida_actual} de vida.")

            if enemigos_detectados:
                print("\n---- ENEMIGOS DETECTADOS ----")
                for mensaje in enemigos_detectados:
                    print(mensaje)
            else:
                print("No hay enemigos en esa área.")

            self.enfriamiento_restante = 2
            break  # acción completada correctamente
