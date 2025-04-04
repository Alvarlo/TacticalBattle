from Clases.Jugador import Jugador
from Clases.Tablero import Tablero

jugador1 = Jugador()
jugador1.crearEquipo()

tablero = Tablero(8,8)

posicionesIniciales = [("Artillero",1,1),("Medico",2,2),("Francotirador",3,3),("Inteligencia",4,4)]

jugador1.posicionarEquipo(tablero,posicionesIniciales)

