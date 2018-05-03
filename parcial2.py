import pygame

size = width, height = [680, 400]
jugadores = pygame.sprite.Group()
reloj = pygame.time.Clock()

class Jugador(pygame.sprite.Sprite):
	"""docstring for Jugador"""
	def __init__(self, matrix):
		pygame.sprite.Sprite.__init__(self)
		self.f = matrix
		self.image = self.f[0][0]
		self.rect = self.image.get_rect()
		self.direction = 0
		self.index = 0

	def update(self):
		if self.direction == 1:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.index >= 11:
				self.index = 0
			self.rect.x += 5


#Recortar sprite
def recortarSprite(nombrearchivo, cantidadX, cantidadY):
	imageSprite = pygame.image.load(nombrearchivo)
	imageInfo = imageSprite.get_rect()
	imageWidth = imageInfo[2]
	imageHeight = imageInfo[3] -200
	corteX = imageWidth / cantidadX
	matrix = []
	corteY = imageHeight / cantidadY
	for y in range(cantidadY):
		matrix.append([])
		for x in range(cantidadX):
			cuadro = imageSprite.subsurface(corteX * x, corteY * y, corteX,corteY)
			matrix[y].append(cuadro)
	return matrix

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode(size)
    matrixKano = recortarSprite('source/homerosprite.png', 16, 39)
    jugador = Jugador(matrixKano)
    jugadores.add(jugador)
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_RIGHT:
            		jugador.direction = 1
     	pantalla.fill([0, 0, 0])
    	jugadores.draw(pantalla)
    	jugadores.update()
    	pygame.display.flip()
    	reloj.tick(10)
