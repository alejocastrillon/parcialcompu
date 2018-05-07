import pygame

size = width, height = [680, 400]
jugadores = pygame.sprite.Group()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(size)
posx = 0
posy = 0

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
			if self.index >= 8:
				self.index = 4
			if self.rect.x <= width - 150:
				self.rect.x += 5
		elif self.direction == 2:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y <= height - 150:
				self.rect.y += 5
		elif self.direction == 3:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y >= 5:
				self.rect.y -= 5

def generateAmbient():
	pantalla.blit(imageFondo, [posx, posy])


#Recortar sprite
def recortarSprite(nombrearchivo, cantidadX, cantidadY):
	imageSprite = pygame.image.load(nombrearchivo)
	imageInfo = imageSprite.get_rect()
	imageWidth = imageInfo[2]
	imageHeight = imageInfo[3]
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
    imageFondo = pygame.image.load('source/fondo.png')
    imagefondoInfo = imageFondo.get_rect()
    imageFondoWidth = imagefondoInfo[2]
    imageFondoHeight = imagefondoInfo[3]
    generateAmbient()
    matrixKano = recortarSprite('source/homerocamina.png', 12, 1)
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
            	elif event.key == pygame.K_DOWN:
            		jugador.direction = 2
            	elif event.key == pygame.K_UP:
            		jugador.direction = 3
            	elif event.key == pygame.K_SPACE:
            		jugador.direction = 0
        if jugador.direction == 1 and jugador.rect.x >= width -150 and posx >= width - imageFondoWidth:
        	posx -= 5
        elif jugador.direction == 2 and jugador.rect.y >= height - 150 and posy >= height- imageFondoHeight:
        	posy -= 5
        elif jugador.direction == 3 and jugador.rect.y >= 20 and posy <= -10:
        	posy += 5
        generateAmbient()
    	  jugadores.draw(pantalla)
    	  jugadores.update()
    	  pygame.display.flip()
    	  reloj.tick(10)
