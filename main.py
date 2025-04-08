from Clases.Jugador import Jugador
from Clases.Tablero import Tablero
from utils import limpiar_terminal

def main():
    
    
    print('¡Bienvenidos a Tactical Battle. A jugar!\n')

    
    input('Turno del Jugador 1. Pulsa intro para comenzar:')
    tableroJugador1 = Tablero(4,4)
    j1 = Jugador(tableroJugador1)
    input('Jugador 1, pulsa terminar tu turno')
    limpiar_terminal()
    

    input('Turno del Jugador 2. Pulsa intro para comenzar:')
    tableroJugador2 = Tablero(4,4)
    j2 = Jugador(tableroJugador2)
    input('Jugador 2, pulsa terminar tu turno')
    limpiar_terminal()


    j1.set_oponente(j2)
    j2.set_oponente(j1)

    final = False
    while not final:
        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = j1.turno()
        if final:
            print('****** El jugador 1 ha ganado la partida! ******')
            return 0
        input('Jugador 1, pulsa intro para terminar tu turno')
        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = j2.turno()
        if final:
            print('****** El jugador 2 ha ganado la partida! ******')
            return 0

        input('Jugador 2, pulsa intro para terminar tu turno')
        limpiar_terminal()












if __name__ == '__main__':
    main()
