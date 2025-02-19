import pygame

# Clase base Buff
class Nerf:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vel = 3
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

    def draw(self, ventana):
        pygame.draw.rect(ventana, self.color, self.rect)

    def movimiento(self):
        self.y += self.vel
        self.rect.y = self.y


# Buff que da vida (verde)
class NerfVida(Nerf):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0))  # Verde

    def aplicar_efecto(self, personaje):
        personaje.vida -= 1


# Buff de velocidad (azul)
class NerfVelocidad(Nerf):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0))  # rojo
        self.duracion = 3000  # 3 segundos de velocidad extra

    def aplicar_efecto(self, personaje):
        personaje.vel -= 1
        pygame.time.set_timer(pygame.USEREVENT + 3, self.duracion)  # Evento para revertir el buff

class NerfBalas(Nerf):
    def __init__(self, x, y):
        super().__init__(x, y, (255,0,0))  # rojo
        self.duracion = 3000  # 3 segundos de balas extra

    def aplicar_efecto(self, contexto_global):
            contexto_global["tiempo_entre_balas"] = 500  # Aumenta el tiempo entre balas
            pygame.time.set_timer(pygame.USEREVENT + 4, self.duracion)  # Evento para revertir el nerf