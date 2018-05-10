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
		self.action = 0
		self.index = 0

		'''Acciones:
		1. Puno
		2. Caminar
		3. Martillo '''

	def update(self):
		if self.direction == 1 and self.action == 2:
			self.image = self.f[1][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.x <= width - 150:
				self.rect.x += 5
		elif self.direction == 2 and self.action == 2:
			self.image = self.f[3][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.x >= 33:
				self.rect.x += -5
		elif self.direction == 3 and self.action == 2:
			self.image = self.f[2][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y >= 10:
				self.rect.y -= 5
		elif self.direction == 4 and self.action == 2:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y <= height - 150:
				self.rect.y += 5

		if self.action == 1:
			if self.direction == 2:
				self.image = self.f[5][self.index]
			else:
				self.image = self.f[4][self.index]
			self.index +=1
			if self.index >=8:
				self.index = 0
				if self.direction == 2:
					self.image = self.f[3][self.index]
				else:
					self.image = self.f[self.direction][self.index]
				self.action = 0
		elif self.action == 3:
			if self.direction == 2:
				self.image = self.f[7][self.index]
			else:
				self.image = self.f[6][self.index]
			self.index +=1
			if self.index >=5:
				self.index = 0
				if self.direction == 2:
					self.image = self.f[3][self.index]
				else:
					self.image = self.f[self.direction][self.index]
				self.action = 0
		'''elif self.action == 1 and self.direction == 2:
			self.image = self.f[5][self.index]
			self.index +=1
			if self.index >=8:
				self.index = 0
				self.image = self.f[3][self.index]
				self.action = 0
				self.direction = 0'''


def generateAmbient():
	pantalla.blit(imageFondo, [posx, posy])


#Recortar sprite
def recortarSprite(nombrearchivo, cantidadX, cantidadY):
	imageSprite = pygame.image.load(nombrearchivo)
	imageInfo = imageSprite.get_rect()
	imageWidth = imageInfo[2]
	imageHeight = imageInfo[3]
<<<<<<< HEAD
	corteX = imageWidth / cantidadX - 1
=======
	corteX = 33
>>>>>>> 2e2ff80618191bfd9e7cb2c02d40dc24463d021e
	matrix = []
	corteY = (imageHeight / cantidadY)
	listaCorte = [8,8,8,8,9,9,6,6]
	for y in range(cantidadY):
		matrix.append([])
		for x in range(listaCorte[y]):
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
<<<<<<< HEAD
    matrixKano = recortarSprite('source/mario.png', 8, 5)
=======
    matrixKano = recortarSprite('source/terminado.png', 8, 8)
>>>>>>> 2e2ff80618191bfd9e7cb2c02d40dc24463d021e
    jugador = Jugador(matrixKano)
    jugadores.add(jugador)
    pygame.display.flip()
    done = False
    while not done:
        for event in pygame.event.get():
<<<<<<< HEAD
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
            	if event.key == pygame.K_RIGHT:
            		jugador.direction = 1
            	elif event.key == pygame.K_b:
            		jugador.direction = 2
            	elif event.key == pygame.K_UP:
            		jugador.direction = 3
            	elif event.key == pygame.K_SPACE:
            		jugador.direction = 0
=======
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				jugador.index = 0
				if event.key == pygame.K_RIGHT:
					jugador.direction = 1
					jugador.action = 2
				elif event.key == pygame.K_LEFT:
					jugador.direction = 2
					jugador.action = 2
				elif event.key == pygame.K_UP:
					jugador.direction = 3
					jugador.action = 2
				elif event.key == pygame.K_DOWN:
					jugador.direction = 4
					jugador.action = 2
				elif event.key == pygame.K_SPACE:
					jugador.direction = 0
				elif event.key == pygame.K_p:
					jugador.action = 1
				elif event.key == pygame.K_m:
					jugador.action = 3

>>>>>>> 2e2ff80618191bfd9e7cb2c02d40dc24463d021e
        if jugador.direction == 1 and jugador.rect.x >= width -150 and posx >= width - imageFondoWidth:
        	posx -= 5
        elif jugador.direction == 4 and jugador.rect.y >= height - 150 and posy >= height- imageFondoHeight:
        	posy -= 5
        elif jugador.direction == 2 and jugador.rect.x>= 20 and posx <= -10:
        	posx += 5
        elif jugador.direction == 3 and jugador.rect.y >= 40 and posy <= -10:
        	posy += 5
        generateAmbient()
    	jugadores.draw(pantalla)
    	jugadores.update()
    	pygame.display.flip()
    	reloj.tick(10)
