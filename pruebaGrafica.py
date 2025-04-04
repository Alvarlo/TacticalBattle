import pygame
import string

#Comienza la partida

# Inicializar
pygame.init()

# Configuración
TAM_CASILLA = 64
FILAS, COLUMNAS = 8, 8
MARGEN_IZQ_SUP = 40
MARGEN_SUP_EXTRA = 40

ANCHO = COLUMNAS * TAM_CASILLA + MARGEN_IZQ_SUP
ALTO = FILAS * TAM_CASILLA + MARGEN_IZQ_SUP + MARGEN_SUP_EXTRA

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS_CLARO = (230, 230, 230)

# Fuente
fuente = pygame.font.SysFont('Arial', 24)
fuente_titulo = pygame.font.SysFont('Arial', 28, bold=True)

# Estado del tablero (None o letra del personaje)
tablero = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Fase de colocación - Tablero Táctico")

# Personaje actual a colocar (puedes cambiar esto luego por selección)
personaje_actual = "G"

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

            col = (x - MARGEN_IZQ_SUP) // TAM_CASILLA
            fila = (y - MARGEN_IZQ_SUP - MARGEN_SUP_EXTRA) // TAM_CASILLA

            if 0 <= fila < FILAS and 0 <= col < COLUMNAS:
                if tablero[fila][col] is None:
                    tablero[fila][col] = personaje_actual

    pantalla.fill(BLANCO)

    # Título
    texto_titulo = fuente_titulo.render("Jugador 1 - Coloca tus personajes", True, NEGRO)
    pantalla.blit(texto_titulo, ((ANCHO - texto_titulo.get_width()) // 2, 5))

    # Letras A-H
    letras = string.ascii_uppercase[:COLUMNAS]
    for i, letra in enumerate(letras):
        texto = fuente.render(letra, True, NEGRO)
        x = MARGEN_IZQ_SUP + i * TAM_CASILLA + TAM_CASILLA // 2 - texto.get_width() // 2
        pantalla.blit(texto, (x, MARGEN_SUP_EXTRA))

    # Números 1–8
    for i in range(FILAS):
        numero = fuente.render(str(i + 1), True, NEGRO)
        y = MARGEN_SUP_EXTRA + MARGEN_IZQ_SUP + i * TAM_CASILLA + TAM_CASILLA // 2 - numero.get_height() // 2
        pantalla.blit(numero, (5, y))

    # Dibujar casillas y personajes
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            x = MARGEN_IZQ_SUP + col * TAM_CASILLA
            y = MARGEN_SUP_EXTRA + MARGEN_IZQ_SUP + fila * TAM_CASILLA
            rect = pygame.Rect(x, y, TAM_CASILLA, TAM_CASILLA)

            color = GRIS_CLARO if (fila + col) % 2 == 0 else BLANCO
            pygame.draw.rect(pantalla, color, rect)
            pygame.draw.rect(pantalla, NEGRO, rect, 1)

            # Dibujar letra si hay personaje
            if tablero[fila][col] is not None:
                letra = fuente.render(tablero[fila][col], True, NEGRO)
                letra_x = x + (TAM_CASILLA - letra.get_width()) // 2
                letra_y = y + (TAM_CASILLA - letra.get_height()) // 2
                pantalla.blit(letra, (letra_x, letra_y))

    pygame.display.flip()

pygame.quit()

