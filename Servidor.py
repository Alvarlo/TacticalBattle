import socket
import threading
import sys
from Clases.Gestion.Cliente import Cliente
from Clases.Gestion.Cola import Cola
from Clases.Partida import Partida
from Clases.Gestion.Ranking import Ranking

# Configuración y carga de ranking
ARCHIVO_RANKING = sys.argv[3]
ranking_global = Ranking()
ranking_global.cargar_desde_archivo(ARCHIVO_RANKING)

# Datos de red
IP = "0.0.0.0"
PORT = int(sys.argv[1])
MAX_PARTIDAS = int(sys.argv[2])

# Lobby y contador de partidas
lobby = Cola()
lock_lobby = threading.Lock()
partidas_en_curso = 0

def manejar_cliente(conn, addr):
    global partidas_en_curso

    try:
        nombre = conn.recv(1024).decode().strip()
        print(f"[+] Conectado: {nombre} desde {addr}")
        cliente = Cliente(nombre, conn)

        with lock_lobby:
            if lobby.esta_vacia():
                lobby.encolar(cliente)
                print(f"[LOBBY] {nombre} esperando rival...")
            else:
                rival = lobby.desencolar()
                print(f"[MATCH] {rival.nombre} vs {cliente.nombre}")
                hilo = threading.Thread(target=iniciar_partida, args=(rival, cliente))
                hilo.start()
                partidas_en_curso += 1

    except Exception as e:
        print(f"[ERROR] Error con {addr}: {e}")
    finally:
        pass

def iniciar_partida(cliente1, cliente2):
    partida = Partida(cliente1, cliente2, ranking_global, ARCHIVO_RANKING)
    partida.start()

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((IP, PORT))
    servidor.listen()
    print(f"[SERVIDOR] Escuchando en {IP}:{PORT}")

    while True:
        conn, addr = servidor.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr)).start()

if __name__ == "__main__":
    iniciar_servidor()

