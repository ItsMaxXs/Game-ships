import pygame

# Clase base Buff
class Buff:
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
class BuffVida(Buff):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 255, 0))  # Verde

    def aplicar_efecto(self, personaje):
        personaje.vida += 1

# Buff de velocidad (azul)
class BuffVelocidad(Buff):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 255, 0))  # Azul
        self.duracion = 3000  # 3 segundos de velocidad extra

    def aplicar_efecto(self, personaje):
        personaje.vel += 2
        pygame.time.set_timer(pygame.USEREVENT + 1, self.duracion)  # Evento para revertir el buff

# Buff de balas (morado)
class BuffBalas(Buff):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 255, 0))  # Morado
        self.duracion = 3000  # 3 segundos de disparo más rápido

    def aplicar_efecto(self, contexto_global):
        contexto_global["tiempo_entre_balas"] = 125  # Reduce el tiempo entre balas
        pygame.time.set_timer(pygame.USEREVENT + 2, self.duracion)  # Evento para revertir el buff
