
import socket
import threading
import pickle
from Clases.Jugador import Jugador
from Clases.Tablero import Tablero

# Crear tablero y jugador (cliente local)
tablero = Tablero(4, 4)
jugador = Jugador(tablero)

def recibir_mensajes(socket_cliente):
    while True:
        try:
            datos = socket_cliente.recv(4096).decode()
            if not datos:
                break

            # Desglosar mensajes por líneas si vienen agrupados
            mensajes = datos.strip().split("\n")
            for mensaje in mensajes:
                mensaje = mensaje.strip()
                print(f"\n[Servidor]: {mensaje}")

                if mensaje.startswith("ACCION:"):
                    accion = mensaje[7:].strip()
                    resultado = jugador.recibirAccion(accion)
                    socket_cliente.sendall(f"RESULTADO:{resultado}\n".encode())

                elif mensaje == "ES_TU_TURNO":
                    realizar_turno(socket_cliente)

                elif mensaje == "ESPERA_TURNO":
                    print("Esperando al otro jugador...")

                elif mensaje == "SALIR":
                    print("La partida ha terminado.")
                    return
        except Exception as e:
            print(f"\n[Desconectado del servidor]: {e}")
            break

def realizar_turno(socket_cliente):
    print("\n🎯 ES TU TURNO 🎯\n")
    accion = jugador.turno()  # Esto muestra resumen, tablero y lanza menú

    if accion == None or accion == "":
        accion = "No hay nada que informar"
    socket_cliente.sendall(accion.encode())  # Envía la acción como string

def main():
    host = input("IP del servidor (localhost para pruebas): ")
    port = int(input("Puerto del servidor: "))
    nombre = input("Tu nombre: ")

    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((host, port))
    socket_cliente.sendall(nombre.encode())

    print("\n[Conectado al servidor, esperando instrucciones...]")

    # Iniciar hilo para recibir mensajes
    hilo_recepcion = threading.Thread(target=recibir_mensajes, args=(socket_cliente,))
    hilo_recepcion.daemon = True
    hilo_recepcion.start()

    # Escuchar entrada por consola (solo para comando SALIR)
    while True:
        try:
            mensaje = input()
            if mensaje.upper() == "SALIR":
                socket_cliente.sendall("SALIR".encode())
                break
        except KeyboardInterrupt:
            break

    socket_cliente.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    main()
