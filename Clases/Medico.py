from .Personaje import Personaje;

class Medico(Personaje):

    def __init__(self,vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo):
        super().__init__(vida_maxima, vida_actual,danyo,posicion,enfriamiento_restante,icono,tipo)



    def esPosibleCurar(self,jugador):
        contador = 0
        for unidad in jugador.equipo:
            if unidad.vida_actual < unidad.vida_maxima and unidad.vida_actual != 0:
                contador = contador + 1
 
        if contador > 0:
            return True
        else:
            return False
        

    def habilidad(self,tablero):
        print("Habilidad: Curar a un compañero herido.")

        unidades_heridas = []

        # Recorremos el tablero completo
        for x in range(tablero.cantidadFilas):
            for y in range(tablero.cantidadColumnas):
                unidad = tablero.tablero[x][y]
                if unidad is not None and unidad.vida_actual < unidad.vida_maxima and unidad != self:
                    unidades_heridas.append({
                        "unidad": unidad,
                        "x": x,
                        "y": y
                    })

        # Mostrar menú
        print("\n--- Compañeros heridos ---")
        for idx, entry in enumerate(unidades_heridas, 1):
            unidad = entry["unidad"]
            coord = f"{chr(ord('A') + entry['y'])}{entry['x'] + 1}"
            print(f"{idx}: {unidad.__class__.__name__} en {coord} ({unidad.vida_actual}/{unidad.vida_maxima} HP)")
        print(f"{len(unidades_heridas)+1}: Cancelar")

        # Esperar selección del jugador
        while True:
            eleccion = input("Selecciona a quién curar (número): ")

            if not eleccion.isdigit():
                print("Por favor, introduce un número válido.")
                continue

            eleccion = int(eleccion)

            if eleccion == len(unidades_heridas) + 1:
                print("Habilidad cancelada.")
                return

            if 1 <= eleccion <= len(unidades_heridas):
                objetivo = unidades_heridas[eleccion - 1]["unidad"]
                objetivo.vida_actual = objetivo.vida_maxima
                print(f"{objetivo.__class__.__name__} ha sido curado completamente.")
                self.enfriamiento_restante = 2
                return
            else:
                print("Opción inválida.")
