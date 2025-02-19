import pygame

class Enemigo:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.vel = 1
        self.color = "purple"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.vida = 3
        self.imagen = pygame.image.load("C:\\Users\\defau\\OneDrive\\Documentos\\Proyectos\\Game\\images\\alien.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        
        
    def draw(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        ventana.blit(self.imagen, (self.x, self.y))
        
        
    def movimiento(self):
        self.y += self.vel
        