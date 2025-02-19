import pygame
import sys

# Inicializar todos los módulos de Pygame
pygame.init()

# Configuraciones de la ventana
ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Naves")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Fuentes
FUENTE = pygame.font.SysFont("comicsans", 30)

# Función para mostrar el menú principal
def mostrar_menu():
    menu_activo = True
    nombre = ""

    while menu_activo:
        VENTANA.fill(NEGRO)
        texto_titulo = FUENTE.render("Juego de Naves", True, BLANCO)
        texto_jugar = FUENTE.render("Presiona 'J' para Jugar", True, BLANCO)
        texto_instrucciones = FUENTE.render("Presiona 'I' para Instrucciones", True, BLANCO)
        texto_salir = FUENTE.render("Presiona 'Esc' para Salir", True, BLANCO)

        VENTANA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))
        VENTANA.blit(texto_jugar, (ANCHO // 2 - texto_jugar.get_width() // 2, ALTO // 2))
        VENTANA.blit(texto_instrucciones, (ANCHO // 2 - texto_instrucciones.get_width() // 2, ALTO // 2 + 50))
        VENTANA.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, ALTO // 2 + 100))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_j:  # Opción para jugar
                    nombre = pedir_nombre()
                    if nombre:
                        menu_activo = False
                elif evento.key == pygame.K_i:  # Opción para instrucciones
                    mostrar_instrucciones()
                elif evento.key == pygame.K_ESCAPE:  # Opción para salir
                    pygame.quit()
                    sys.exit()

    return nombre


# Función para pedir el nombre del jugador
def pedir_nombre():
    nombre = ""
    input_activado = True
    while input_activado:
        VENTANA.fill(NEGRO)
        texto_nombre = FUENTE.render("Introduce tu nombre: " + nombre, True, BLANCO)
        VENTANA.blit(texto_nombre, (ANCHO // 2 - texto_nombre.get_width() // 2, ALTO // 3))
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Cuando se presiona Enter, terminamos de pedir el nombre
                    input_activado = False
                elif evento.key == pygame.K_BACKSPACE:  # Borrar un caracter
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode  # Agregar el carácter presionado

    return nombre


# Función para mostrar las instrucciones
def mostrar_instrucciones():
    instrucciones_activo = True
    while instrucciones_activo:
        VENTANA.fill(NEGRO)

        # Título
        texto_titulo = FUENTE.render("Instrucciones del Juego", True, AZUL)
        VENTANA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 10 - 40))

        # Controles
        texto_controles = FUENTE.render("Controles:", True, BLANCO)
        texto_1 = FUENTE.render("Flechas para mover la nave", True, BLANCO)
        texto_2 = FUENTE.render("Espacio para disparar", True, BLANCO)
        
        # Objetivos
        texto_objetivos = FUENTE.render("Objetivos:", True, BLANCO)
        texto_3 = FUENTE.render("Destruye enemigos y recoge buffs", True, BLANCO)
        texto_4 = FUENTE.render("Evita que los enemigos toquen tu nave", True, BLANCO)

        # Buffs y Nerfs
        texto_buff_nerf = FUENTE.render("Buffs y Nerfs:", True, BLANCO)
        texto_5 = FUENTE.render("Buffs: Mejoran tu nave (Verde)", True, BLANCO)
        texto_6 = FUENTE.render("Nerfs: Dañan tu nave (Rojo)", True, BLANCO)
        texto_7 = FUENTE.render("Ambos son aleatorios y aparecen en el campo de juego.", True, BLANCO)

        # Consejos
        texto_consejos = FUENTE.render("Consejos:", True, BLANCO)
        texto_8 = FUENTE.render("Recoge buffs para mejorar tu nave", True, BLANCO)
        texto_9 = FUENTE.render("Evita los nerfs que te perjudican", True, BLANCO)

        # Mostrar texto
        VENTANA.blit(texto_controles, (ANCHO // 2 - texto_controles.get_width() // 2, ALTO // 5 - 40))
        VENTANA.blit(texto_1, (ANCHO // 2 - texto_1.get_width() // 2, ALTO // 5 + 0))
        VENTANA.blit(texto_2, (ANCHO // 2 - texto_2.get_width() // 2, ALTO // 5 + 40))
        
        VENTANA.blit(texto_objetivos, (ANCHO // 2 - texto_objetivos.get_width() // 2, ALTO // 5 + 100))
        VENTANA.blit(texto_3, (ANCHO // 2 - texto_3.get_width() // 2, ALTO // 5 + 140))
        VENTANA.blit(texto_4, (ANCHO // 2 - texto_4.get_width() // 2, ALTO // 5 + 180))
        
        VENTANA.blit(texto_buff_nerf, (ANCHO // 2 - texto_buff_nerf.get_width() // 2, ALTO // 5 + 240))
        VENTANA.blit(texto_5, (ANCHO // 2 - texto_5.get_width() // 2, ALTO // 5 + 280))
        VENTANA.blit(texto_6, (ANCHO // 2 - texto_6.get_width() // 2, ALTO // 5 + 320))
        VENTANA.blit(texto_7, (ANCHO // 2 - texto_7.get_width() // 2, ALTO // 5 + 360))

        VENTANA.blit(texto_consejos, (ANCHO // 2 - texto_consejos.get_width() // 2, ALTO // 5 + 420))
        VENTANA.blit(texto_8, (ANCHO // 2 - texto_8.get_width() // 2, ALTO // 5 + 460))
        VENTANA.blit(texto_9, (ANCHO // 2 - texto_9.get_width() // 2, ALTO // 5 + 500))

        # Botón de regresar
        texto_regresar = FUENTE.render("Presiona 'Esc' para Regresar", True, BLANCO)
        VENTANA.blit(texto_regresar, (ANCHO // 2 - texto_regresar.get_width() // 2, ALTO // 5 + 540))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Regresar al menú principal
                    instrucciones_activo = False

# Lógica principal
if __name__ == "__main__":
    nombre = mostrar_menu()
    if nombre:
        print(f"El jugador {nombre} comenzará el juego.")
        # Aquí puedes llamar a la función para iniciar el juego
    else:
        print("Juego cerrado.")
    pygame.quit()
