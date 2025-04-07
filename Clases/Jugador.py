from Clases.Artillero import Artillero
from Clases.Francotirador import Francotirador
from Clases.Inteligencia import Inteligencia
from Clases.Medico import Medico
import random

class Jugador:
    def __init__(self,tablero):
        self.oponente = None
        self.equipo = None
        self.informe = ""
        self.tablero = tablero

        self.crearEquipo()
        self.posicionarEquipo()


    
    def set_oponente(self, value):
        self.oponente = value
   


    def resumenDelEquipo(self):
        print("\n---- SITUACION DEL EQUIPO ----")
        for unidad in self.equipo:
            x = unidad.posicion["x"]
            y = unidad.posicion["y"]
            letra_columna = chr(ord('A') + y)  # convierte 0 → A, 1 → B, etc.
            numero_fila = x + 1                # convierte 0 → 1, etc.
            print(f"{unidad.__class__.__name__} está en {letra_columna}{numero_fila} [Vida {unidad.vida_actual}/{unidad.vida_maxima}]")


    def mostrar_menu_acciones(self):
        print("\n----- MENÚ DE ACCIONES -----")
        opcion = 1
        opciones = {}

        for unidad in self.equipo:
            print(f"{opcion}: Mover ({unidad.__class__.__name__})")
            opciones[opcion] = (unidad, "mover")
            opcion += 1

            if unidad.__class__.__name__ == "Artillero" and unidad._enfriamiento_restante == 0:
                print(f"{opcion}: Disparar en área (2x2). Daño 1. ({unidad.__class__.__name__})")
                opciones[opcion] = (unidad, "habilidad")
                opcion += 1
            elif unidad.__class__.__name__ == "Francotirador" and unidad._enfriamiento_restante == 0:
                print(f"{opcion}: Disparar a una celda. Daño 3. ({unidad.__class__.__name__})")
                opciones[opcion] = (unidad, "habilidad")
                opcion += 1
            elif unidad.__class__.__name__ == "Inteligencia" and unidad._enfriamiento_restante == 0:
                print(f"{opcion}: Revelar enemigos en área 2x2. ({unidad.__class__.__name__})")
                opciones[opcion] = (unidad, "habilidad")
                opcion += 1
            elif unidad.__class__.__name__ == "Medico" and unidad._enfriamiento_restante == 0:
                print(f"{opcion}: Curar a un compañero. ({unidad.__class__.__name__})")
                opciones[opcion] = (unidad, "habilidad")
                opcion += 1

        return opciones

    #turno(): función para gestionar la lógica del turno de un jugador. 
    #Devuelve un bool indicando si se ha llegado al final de la partida.
    def turno(self):
        self.resumenDelEquipo()
        self.tablero.situacionDelTablero()
        self.realizarAccion()
        
        return True
    
    #realizar_accion(): permite al jugador elegir una acción de entre las acciones disponibles 
    #de los miembros vivos del equipo mediante un menú. La ejecuta y devuelve su código 
    #correspondiente. La llama el jugador en activo.
    def realizarAccion(self):
        while True:
            opciones = self.mostrar_menu_acciones()

            try:
                seleccion = int(input("Selecciona una opción: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if seleccion in opciones:
                unidad, accion = opciones[seleccion]

                if accion == "mover":
                    # Obtener posición actual
                    x = unidad.posicion["x"]
                    y = unidad.posicion["y"]
                    letra_columna = chr(ord('A') + y)
                    numero_fila = x + 1

                    while True:
                        coordenada = input(f"¿A qué coordenada quieres mover a {unidad.__class__.__name__}? (Posición actual: {letra_columna}{numero_fila})\nEscribe 'volver' para regresar al menú: ").upper()

                        if coordenada == "VOLVER":
                            break  # vuelve al menú de acciones

                        if len(coordenada) < 2 or not coordenada[1:].isdigit():
                            print("Coordenada inválida.")
                            continue

                        fila = int(coordenada[1:]) - 1
                        columna = ord(coordenada[0]) - ord('A')

                        if self.tablero.esPosibleMoverAqui(fila, columna):
                            unidad.mover(coordenada, self.tablero)
                            return  # acción válida realizada → salimos del método
                        else:
                            print("No se puede mover a esa posición. Está ocupada o fuera del tablero.")

                elif accion == "habilidad":
                    unidad.usar_habilidad(self.tablero)
                    return  # acción válida realizada → salimos del método
            else:
                print("Opción no válida. Intenta de nuevo.")




        
    #recibir_accion(str): dependiendo del código de acción recibido por parámetro, actualizar 
    #el estado del equipo si es necesario, actualizar el informe y devolver el resultado de la 
    #acción. La llama el jugador inactivo.
    # El retorno de esta función puede ser:
    # o None, si no hay nada que reportar porque la acción del jugador activo no afecta al tablero.
    # o Un diccionario con dos keys: una para informar del resultado al enemigo y otra 
    # para indicar si la partida ha terminado como resultado de la acción recibida.

    def recibirAccion(self,accion):
        print(accion)
        return accion
    
    #crear_equipo():función auxiliar para crearlos personajes y añadirlos a la lista del equipo.
    def crearEquipo(self):
        #Los dos jugadores empiezan con el mismo equipo:
        #   1 francotirador (dispara y quita 3 de daño)
        #   1 medico (cura al )
        #   1 artillero (dispara en area de 2x2 quita uno de daño)
        #   1 inteligencia (revela si hay jugadores enemigos en un area de 2x2)

        # Existen cuatro tipos de personaje, cada uno de ellos con una habilidad propia:
        # 
        # • Médico:
        #   - Habilidad: Curar a un miembro vivo del equipo, restituyendo su vida al máximo.
        #   - Vida máxima: 1
        #   - Tipo: No militar
        # 
        # • Inteligencia:
        #   - Habilidad: Explorar un área 2x2 del tablero enemigo, revelando la posición de las unidades en la zona.
        #   - Vida máxima: 2
        #   - Tipo: No militar
        # 
        # • Artillero:
        #   - Habilidad: Disparar en un área 2x2 y aplicar 1 de daño a los objetivos dentro de esa zona.
        #   - Vida máxima: 2
        #   - Tipo: Militar
        # 
        # • Francotirador:
        #   - Habilidad: Disparar a una celda específica y eliminar al objetivo si se encuentra en ella.
        #   - Vida máxima: 3
        #   - Tipo: Militar




        artillero = Artillero(2,2,1,{},0,"icons/inteligencia.png","M")
        francotirador = Francotirador(3,3,3,{},0,"icons/inteligencia.png","M")
        medico = Medico(2,2,0,{},0,"icons/inteligencia.png","NM")
        inteligencia = Inteligencia(1,1,0,{},0,"icons/inteligencia.png","NM")

        self.equipo = [artillero,francotirador,medico,inteligencia]
        print("Equipo Creado")


    def obtener_personaje_por_nombre(self,nombre_clase, lista_de_personajes):
        for personaje in lista_de_personajes:
            if personaje.__class__.__name__ == nombre_clase:
                return personaje
        return False
    

    def generarPosicionesIniciales(self):
        tamaño_tablero = 4
        tipos_unidades = ["Artillero", "Medico", "Francotirador", "Inteligencia"]
        posiciones_ocupadas = []
        posicionesIniciales = []

        for tipo in tipos_unidades:
            while True:
                x = random.randint(0, tamaño_tablero - 1)
                y = random.randint(0, tamaño_tablero - 1)
                nueva_pos = (x, y)

                if nueva_pos not in posiciones_ocupadas:
                    posiciones_ocupadas.append(nueva_pos)
                    posicionesIniciales.append((tipo, x, y))
                    break  

        return posicionesIniciales

    
    #posicionar_equipo(): función auxiliar para permitir al usuario colocar a los miembros del equipo sobre el tablero
    def posicionarEquipo(self):
        
        tablero = self.tablero
        posiciones=self.generarPosicionesIniciales()
        
        for posicion in posiciones:
            nombre = posicion[0]
            x = posicion[1]
            y = posicion[2]

            #Primero recorremos nuestro tablero y vemos si las posiciones enviadas son validas para colocar nuestros personajes
            #En caso de no ser validas retornaremos false
            if not tablero.esPosibleMoverAqui(x, y):
                print(f"No es posible colocar el {nombre} en la posición ({x}, {y})")
                return False
            
            #Si la posicion enviada es valida y existe un personaje con ese nombre lo colocamos
            else:
                if self.obtener_personaje_por_nombre(nombre,self.equipo):
                    unidad= self.obtener_personaje_por_nombre(nombre,self.equipo)

                    #Actualizando nuestro tablero
                    tablero.colocarUnidad(unidad, x, y)
                    #Actualizamos el atributo posicion de nuestros personajes
                    unidad.set_posicion(x,y)
                else:
                    print(f"No existe en mi equipo un personaje con el nombre de {nombre}")
                    return False
            
        
        #Una vez comprobadas que las posiciones son correctas pasamos a posicionar los personajes
        #Actualizando nuestro tablero y Actualizando el atributo posicion de nuestros personajes


            
        

