import pygame

class Disparo:
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.ancho = 40
        self.alto = 40
        self.vel = 10
        self.color = "white"
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.velocidad_disparo = 250
        
        # Agregar la imagen para el disparo
        self.imagen = pygame.image.load("C:\\Users\\defau\\OneDrive\\Documentos\\Proyectos\\Game\\images\\fuego.png")  # Asegúrate de tener esta imagen en la carpeta 'images'
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))  # Escalar la imagen para ajustarla
        self.imagen = pygame.transform.rotate(self.imagen, 90)

    def draw(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        ventana.blit(self.imagen, (self.x, self.y))

    def movimiento(self):
        self.y -= self.vel
