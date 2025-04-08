from .Personaje import Personaje;

class Francotirador(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self, tablero):
        tablero.situacionDelTablero()
        print("Ataca en 1 celda y quita 3 de vida")

        while True:
            coordenada = input("Indica la coordenada que quieres atacar o escribe 'volver': ").upper()

            if coordenada == "VOLVER":
                print("Cancelando habilidad del Francotirador.")
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

            objetivo = tablero.tablero[fila][columna]
            resultados = []

            if objetivo is not None:
                objetivo.vida_actual -= 3
                objetivo.vida_actual = max(0, objetivo.vida_actual)
                coord = f"{chr(ord('A') + columna)}{fila + 1}"
                resultados.append(f"Impacto en {coord} → {objetivo.__class__.__name__} recibe 3 de daño. Vida restante: {objetivo.vida_actual}")

                if objetivo.vida_actual <= 0:
                    resultados.append(f"{objetivo.__class__.__name__} ha sido eliminado.")
                    tablero.tablero[fila][columna] = None
            else:
                resultados.append(f"El ataque no causado ningun daño (La casilla estaba vacía)")
                
          

            print("\n--- Resultado del disparo del Francotirador ---")
            for mensaje in resultados:
                print(mensaje)

            self.enfriamiento_restante = 2
            break  # Acción realizada correctamente


            