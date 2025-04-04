from Clases.Artillero import Artillero
from Clases.Francotirador import Francotirador
from Clases.Inteligencia import Inteligencia
from Clases.Medico import Medico

class Jugador:
    def __init__(self):
        self.oponente = None
        self.equipo = None
        self.informe = ""

   
    #turno(): función para gestionar la lógica del turno de un jugador. 
    #Devuelve un bool indicando si se ha llegado al final de la partida.
    def turno(self):
        print("turno")
        return True
    
    #realizar_accion(): permite al jugador elegir una acción de entre las acciones disponibles 
    #de los miembros vivos del equipo mediante un menú. La ejecuta y devuelve su código 
    #correspondiente. La llama el jugador en activo.
    def realizarAccion(self):
        print("accion")
        return "accion"
    
    #recibir_accion(str): dependiendo del código de acción recibido por parámetro, actualizar 
    #el estado del equipo si es necesario, actualizar el informe y devolver el resultado de la 
    #acción. La llama el jugador inactivo.
    # El retorno de esta función puede ser:
    # o None, si no hay nada que reportar porque la acción del jugador activo no afecta al tablero.
    # o Un diccionario con dos keys: una para informar del resultado al enemigo y otra 
    # para indicar si la partida ha terminado como resultado de la acción recibida.

    def realizarAccion(self,accion):
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
    
    #posicionar_equipo(): función auxiliar para permitir al usuario colocar a los miembros del equipo sobre el tablero
    def posicionarEquipo(self,tablero,posiciones):

        
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
                    unidad.posicion = {"x": x, "y": y}
                else:
                    print(f"No existe en mi equipo un personaje con el nombre de {nombre}")
                    return False
            
        
        #Una vez comprobadas que las posiciones son correctas pasamos a posicionar los personajes
        #Actualizando nuestro tablero y Actualizando el atributo posicion de nuestros personajes


            
        

