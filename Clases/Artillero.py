from .Personaje import Personaje;

class Artillero(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)


    def habilidad(self, tablero):

        tablero.situacionDelTablero()
        print("Ataca en 2x2 y quita 1 de vida a enemigos en el área.")
        
        while True:
            coordenada = input("Indica la coordenada de la esquina superior izquierda en la que disparar (área 2x2) o escribe 'volver': ").upper()

            if coordenada == "VOLVER":
                print("Cancelando habilidad del Artillero.")
                return

            if len(coordenada) < 2 or not coordenada[1:].isdigit():
                print("Coordenada inválida.")
                continue

            fila = int(coordenada[1:]) - 1
            columna = ord(coordenada[0]) - ord('A')

            # Validar que el área 2x2 no se salga del tablero
            if fila < 0 or columna < 0 or fila + 1 >= tablero.cantidadFilas or columna + 1 >= tablero.cantidadColumnas:
                print("El área 2x2 se sale del tablero.")
                continue

            # Ejecutar el ataque
            enemigos_afectados = 0
            resultados = []

            for dx in range(2):
                for dy in range(2):
                    objetivo = tablero.tablero[fila + dx][columna + dy]
                    if objetivo is not None:
                        objetivo.vida_actual -= 1
                        enemigos_afectados += 1

                        coord = f"{chr(ord('A') + columna + dy)}{fila + dx + 1}"
                        resultados.append(f"Impacto en {coord} → {objetivo.__class__.__name__} recibe 1 de daño. Vida restante: {objetivo.vida_actual}")

                        if objetivo.vida_actual <= 0:
                            resultados.append(f"{objetivo.__class__.__name__} ha sido eliminado.")
                            tablero.tablero[fila + dx][columna + dy] = None

            # Mostrar resultados al final

            print("\n---- RESULTADO DE LA ACCIÓN ----")
            if resultados: 
                for mensaje in resultados:
                    print(mensaje)


            if enemigos_afectados == 0:
                print("No había enemigos en el área.")
            
            self.enfriamiento_restante = 2
            break
