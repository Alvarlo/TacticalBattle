

class Tablero:
    
    def __init__(self,cantidadFilas,cantidadColumnas):
        self.tablero = []
        
        self.cantidadFilas=cantidadFilas
        self.cantidadColumnas=cantidadColumnas


        for fila in range(cantidadFilas):
            #Crea fila vacia
            nueva_fila = []
            for col in range(cantidadColumnas):
                #dentro de la fila creada anteriormente añado un elemento vacio por cada columna
                nueva_fila.append(None)  
            self.tablero.append(nueva_fila)


    def colocarUnidad(self, unidad, x, y):
        self.tablero[x][y] = unidad

    def esPosibleMoverAqui(self,x,y):
        # Aseguramos que la posición esté dentro del rango válido
        if 0 <= x < len(self.tablero) and 0 <= y < len(self.tablero[0]):
            if self.tablero[x][y] is None:
                return True
            else:
                return False
        else:
            print("Posición fuera del tablero.")
            return False
        
   