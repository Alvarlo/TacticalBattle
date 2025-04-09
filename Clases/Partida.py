import threading
import pickle
from .Jugador import Jugador
from .Tablero import Tablero

class Partida(threading.Thread):
    def __init__(self, jugador1, jugador2):
        super().__init__()
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.jugadores = [jugador1, jugador2]
        self.juego_activo = True

    def enviar_a_ambos(self, mensaje):
        try:
            self.jugador1.socket.sendall(mensaje.encode())
            self.jugador2.socket.sendall(mensaje.encode())
        except:
            self.juego_activo = False

    def run(self):
        try:
            # Crear instancias de Jugador con sus tableros y equipos
            tableroJugador1 = Tablero(4, 4)
            tableroJugador2 = Tablero(4, 4)
            j1 = Jugador(tableroJugador1)
            j2 = Jugador(tableroJugador2)

            self.jugador1.jugador = j1
            self.jugador2.jugador = j2

            # Informar a ambos jugadores
            self.jugador1.socket.sendall(f"Empiezas la partida contra {self.jugador2.nombre}. Eres el Jugador 1.\n".encode())
            self.jugador2.socket.sendall(f"Empiezas la partida contra {self.jugador1.nombre}. Eres el Jugador 2.\n".encode())

            turno = 0
            while self.juego_activo:
                jugador_activo = self.jugadores[turno % 2]
                jugador_esperando = self.jugadores[(turno + 1) % 2]

                jugador_activo.socket.sendall("ES_TU_TURNO\n".encode())
                jugador_esperando.socket.sendall("ESPERA_TURNO\n".encode())

                # Recibir acción del jugador activo
                accion = jugador_activo.socket.recv(1024).decode().strip()
                print("Acción recibida:", accion)

                if accion == "SALIR":
                    self.juego_activo = False
                    break

                # Reenviar al otro jugador
                jugador_esperando.socket.sendall(f"ACCION:{accion}\n".encode())

                # Esperar respuesta estructurada (con pickle)
                resultado_bytes = jugador_esperando.socket.recv(4096)
                resultado = pickle.loads(resultado_bytes)
                print("Resultado recibido:", resultado)

                # Enviar mensaje al jugador activo
                jugador_activo.socket.sendall(f"RESULTADO:{resultado['mensaje']}\n".encode())

                # Si la partida terminó
                if resultado.get("fin_partida"):
                    self.juego_activo = False
                    jugador_activo.socket.sendall("GANASTE\n".encode())
                    jugador_esperando.socket.sendall("PERDISTE\n".encode())
                    break

                turno += 1

        except Exception as e:
            print(f"[ERROR EN PARTIDA] {e}")
        finally:
            self.jugador1.socket.close()
            self.jugador2.socket.close()
            print(f"[PARTIDA] Terminada entre {self.jugador1.nombre} y {self.jugador2.nombre}")
