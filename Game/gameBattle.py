import pygame
import sys
import random
from personaje import Personaje
from enemigo import Enemigo
from Disparo import Disparo
from menu import mostrar_menu
from buff import BuffVida, BuffVelocidad, BuffBalas
from nerfs import NerfVida, NerfVelocidad, NerfBalas

pygame.init()

ANCHO = 1000
ALTO = 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de naves")

FPS = 180
FUENTE = pygame.font.SysFont("comicsans", 30)

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0,255,0)
ROJO = (255,0,0)

puntuacion = 0

reloj = pygame.time.Clock()
tiempo_pasado = 0
tiempo_espera = 1500

cubo = Personaje(450, 750)

enemigos = [Enemigo(750 / 2, 100)]
disparos = []
buffs = []
nerfs = []

ultima_bala = 0
tiempo_entre_balas = 250
ultimo_buff = 0
nivel = 1

def gestionar_Teclas(teclas):
    if teclas[pygame.K_LEFT]:
        if cubo.x >= 0:
            cubo.x -= cubo.vel
    if teclas[pygame.K_RIGHT]:
        if cubo.x + cubo.ancho <= ANCHO:
            cubo.x += cubo.vel
    if teclas[pygame.K_UP]:
        if cubo.y >= 0:
            cubo.y -= cubo.vel
    if teclas[pygame.K_DOWN]:
        if cubo.y <= 750:
            cubo.y += cubo.vel
    if teclas[pygame.K_SPACE]:
        crear_disparo()


def crear_disparo():
    global ultima_bala, tiempo_entre_balas
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        disparos.append(Disparo(cubo.rect.centerx, cubo.rect.centery))
        ultima_bala = pygame.time.get_ticks()
        
def repetir_nivel():
    global nivel, puntuacion, cubo, enemigos, disparos, buffs, nerfs, puntuacion, ultima_bala, tiempo_entre_balas, ultimo_buff
    puntuacion = 0
    cubo = Personaje(450, 750)  
    enemigos = [Enemigo(ANCHO / 2, 100)]  
    disparos = [] 
    buffs = []  
    nerfs = []  
    puntuacion = 0  
    ultima_bala = 0  
    tiempo_entre_balas = 250  
    ultimo_buff = 0

def Subir_nivel():
    global nivel, puntuacion, cubo, enemigos, disparos, buffs, nerfs, puntuacion, ultima_bala, tiempo_entre_balas, ultimo_buff, tiempo_espera
    nivel += 1
    puntuacion = 0
    cubo = Personaje(450, 750)  
    enemigos = [Enemigo(ANCHO / 2, 100)]  
    disparos = [] 
    buffs = []  
    nerfs = []  
    puntuacion = 0  
    ultima_bala = 0  
    tiempo_entre_balas = 250  
    ultimo_buff = 0
    tiempo_espera = tiempo_espera - 250

def reiniciar_juego(nombre):
    # Reiniciar todos los parámetros del juego (puntuación, vida, enemigos, etc.)
    global cubo, enemigos, disparos, buffs, nerfs, puntuacion, ultima_bala, tiempo_entre_balas, ultimo_buff, nivel
    cubo = Personaje(450, 750)  
    enemigos = [Enemigo(ANCHO / 2, 100)]  
    disparos = [] 
    buffs = []  
    nerfs = []  
    puntuacion = 0  
    ultima_bala = 0  
    tiempo_entre_balas = 250  
    ultimo_buff = 0
    nivel = 1
    iniciar_juego(nombre)

def mostrar_ventana_confirmacion():
    ventana_confirmacion = True
    opcion_seleccionada = 0  # 0: Repetir nivel, 1: Empezar desde 0, 2: Salir

    while ventana_confirmacion:
        VENTANA.fill(NEGRO)

        # Título
        texto_titulo = FUENTE.render("¿Qué deseas hacer?", True, BLANCO)
        VENTANA.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, ALTO // 4))

        # Opciones del menú
        opciones = ["Repetir nivel", "Empezar desde 0", "Salir"]
        colores = [VERDE if opcion_seleccionada == i else BLANCO for i in range(3)]

        # Mostrar opciones en pantalla
        for i, opcion in enumerate(opciones):
            texto_opcion = FUENTE.render(opcion, True, colores[i])
            y_pos = ALTO // 2 + i * 40  # Espaciado vertical entre opciones
            VENTANA.blit(texto_opcion, (ANCHO // 2 - texto_opcion.get_width() // 2, y_pos))

        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    opcion_seleccionada = (opcion_seleccionada + 1) % 3
                elif evento.key == pygame.K_UP:
                    opcion_seleccionada = (opcion_seleccionada - 1) % 3
                elif evento.key == pygame.K_RETURN:
                    if opcion_seleccionada == 0:
                        return "repetir"
                    elif opcion_seleccionada == 1:
                        return "reiniciar"
                    elif opcion_seleccionada == 2:
                        return "salir"

        pygame.display.update()

def iniciar_juego(nombre):
    global vida, puntuacion, nivel, ultimo_buff
    jugando = True
    tiempo_pasado = 0

    while jugando and cubo.vida > 0:
        tiempo_pasado += reloj.tick(FPS)

        if tiempo_pasado >= tiempo_espera:
            tiempo_pasado = 0
            enemigos.append(Enemigo(random.randint(0, ANCHO), 0))

        #aumentar_dificultad()  # Verifica si el jugador debe subir de nivel
        
        if puntuacion % 2 == 0 and puntuacion != ultimo_buff:
            tipo_buff = random.choice([NerfVelocidad, NerfBalas, BuffVida, BuffVelocidad, BuffBalas, NerfVida, NerfVelocidad])
            buffs.append(tipo_buff(random.randint(0, ANCHO), 0))
            ultimo_buff = puntuacion

        eventos = pygame.event.get()
        teclas = pygame.key.get_pressed()

        texto_vidas = FUENTE.render("Vidas: " + str(cubo.vida), True, BLANCO)
        texto_puntos = FUENTE.render("Puntos: " + str(puntuacion), True, BLANCO)
        texto_nivel = FUENTE.render("Nivel: " + str(nivel), True, BLANCO)

        gestionar_Teclas(teclas)

        cubo.rect = pygame.Rect(cubo.x, cubo.y, cubo.ancho, cubo.alto)

        for evento in eventos:
            global tiempo_entre_balas

            if evento.type == pygame.QUIT:
                jugando = False
            elif evento.type == pygame.USEREVENT + 1:
                cubo.vel -= 2  # Revertir la velocidad
            elif evento.type == pygame.USEREVENT + 2:
                tiempo_entre_balas = 250  # Revertir el tiempo entre balas
            elif evento.type == pygame.USEREVENT + 3:
                cubo.vel = cubo.vel_original  # Restaurar la velocidad original
            elif evento.type == pygame.USEREVENT + 4:
                tiempo_entre_balas = 250  # Revertir el tiempo entre balas

        VENTANA.fill(NEGRO)
        cubo.draw(VENTANA)

        for enemigo in enemigos:
            enemigo.draw(VENTANA)
            enemigo.movimiento()

            if pygame.Rect.colliderect(cubo.rect, enemigo.rect):
                cubo.vida -= 1
                enemigos.remove(enemigo)

            if enemigo.y > ALTO:
                enemigos.remove(enemigo)
                cubo.vida -= 1

        for disparo in disparos:
            disparo.draw(VENTANA)
            disparo.movimiento()
            
            if disparo.y < 0:
                disparos.remove(disparo)

            for enemigo in enemigos:
                if pygame.Rect.colliderect(disparo.rect, enemigo.rect):
                    enemigo.vida -= 1
                    if enemigo.vida <= 0:
                        puntuacion += 1
                        enemigos.remove(enemigo)
                    disparos.remove(disparo)
                    
        for buff in buffs:
            buff.draw(VENTANA)
            buff.movimiento()

            if pygame.Rect.colliderect(cubo.rect, buff.rect):
                if isinstance(buff, BuffBalas):
                    buff.aplicar_efecto(globals())  # Pasamos el contexto global para modificar tiempo_entre_balas
                else:
                    buff.aplicar_efecto(cubo)  # Para BuffVelocidad o BuffVida
                buffs.remove(buff)
                
            if buff.y > ALTO:
                buffs.remove(buff)
                
        for nerf in nerfs:
            nerf.draw(VENTANA)
            nerf.movimiento()

            if pygame.Rect.colliderect(cubo.rect, nerf.rect):
                if isinstance(nerf, NerfBalas):
                    nerf.aplicar_efecto(globals())  # Pasamos el contexto global para modificar tiempo_entre_balas
                else:
                    nerf.aplicar_efecto(cubo)  
                nerfs.remove(nerf)
                
            if nerf.y > ALTO:    
                nerfs.remove(nerf) 
            
        VENTANA.blit(texto_vidas, (10, 10))
        VENTANA.blit(texto_puntos, (10, 40))
        VENTANA.blit(texto_nivel, (10, 70))  # Mostrar el nivel

        pygame.display.update()
        
        if cubo.vida <= 0:
            resultado = mostrar_ventana_confirmacion()
            if resultado == "reiniciar":
                reiniciar_juego(nombre)
            elif resultado == "salir":
                jugando = False  # Salir del juego
            elif resultado == "repetir":
                repetir_nivel()
                                
        if puntuacion == 5:
            Subir_nivel()

    
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre}: {puntuacion}\n")


# Lógica principal
nombre = mostrar_menu()
if nombre:
    iniciar_juego(nombre)
else:
    print("Juego cerrado.")
pygame.quit()
sys.exit()