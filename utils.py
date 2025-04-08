import os

def limpiar_terminal():
    #print(chr(27) + "[2J")
    os.system('cls' if os.name == 'nt' else 'clear')


  