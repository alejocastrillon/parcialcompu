import pygame
import json
from math import *

size = width, height = [680, 400]
jugadores = pygame.sprite.Group()
enemigosBowser = pygame.sprite.Group()
todos = pygame.sprite.Group()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode(size)
posx = 0
posy = 0
listcollide =[]
BLANCO = [255,255,255]
NEGRO = [0,0,0]
AZUL = [0,0,255]
ROJO = [255,0,0]
pygame.mixer.init(44100, -16, 2, 2048)
golpe = pygame.mixer.Sound("source/Sounds/punch.ogg")
movement = pygame.mixer.Sound("source/Sounds/walk.ogg")
fondo = pygame.mixer.Sound("source/Sounds/musicfondo.ogg")

def readerFileCollide():
	with open('source/fondo.json') as col:
		data = json.load(col)
		cantidadX = data["layers"][1]["width"]
		cantidadY = data["layers"][1]["height"]
		listcol = data["layers"][1]["data"]
		dpx = 0
		dpy = 0
		listcollide.append([])
		for x in listcol:
			if dpx == cantidadX:
				dpx = 0
				dpy += 1
				listcollide.append([])
			listcollide[dpy].append(x)
			dpx += 1

def validateMove(dx, dy):
	print "data received: ", listcollide[dy][dx]
	if listcollide[dy][dx] == 0:
		print "data: ", listcollide[dy][dx]
		return True
	else:
		return False

class Jugador(pygame.sprite.Sprite):
	"""docstring for Jugador"""
	def __init__(self, matrix,posx,posy):
		pygame.sprite.Sprite.__init__(self)
		self.f = matrix
		self.image = self.f[0][0]
		self.rect = self.image.get_rect()
		self.direction = 0
		self.action = 0
		self.index = 0
		self.matrixposx = int(round(self.rect.x / 32))
		self.matrixposy = int(round(self.rect.y / 32))
		self.rect.x = posx
		self.rect.y = posy
		'''Acciones:
		1. Puno
		2. Caminar
		3. Martillo '''

	def update(self):
		self.matrixposx = int(round(self.rect.x / 32))
		self.matrixposy = int(round(self.rect.y / 32))
		print self.matrixposx, self.matrixposy


		if self.direction == 1 and self.action == 2:
			self.image = self.f[1][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.x <= width - 150:
				if validateMove(int(ceil((self.rect.x + abs(posx) + 28) / 32)), int(ceil((self.rect.y + abs(posy) + 20) / 32))):
					self.rect.x += 5
		elif self.direction == 2 and self.action == 2:
			self.image = self.f[3][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.x >= 20:
				if validateMove(int(ceil((self.rect.x + abs(posx)) / 32)), int(ceil((self.rect.y + abs(posy) + 20) / 32))):
					self.rect.x += -5
		elif self.direction == 3 and self.action == 2:
			self.image = self.f[2][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y >= 30 :
				if validateMove(int(ceil((self.rect.x + abs(posx) + 16) / 32)), int(ceil((self.rect.y + abs(posy) + 16) / 32))):
					self.rect.y -= 5
		elif self.direction == 4 and self.action == 2:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.index >= 8:
				self.index = 4
			if self.rect.y <= height - 80:
				if validateMove(int(ceil((self.rect.x + abs(posx) + 16) / 32)), int(ceil((self.rect.y + abs(posy) + 36) / 32))):
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

class BowserEnemy(pygame.sprite.Sprite):
	"""docstring for BowserEnemy"""
	def __init__(self, matrix):
		pygame.sprite.Sprite.__init__(self)
		self.f = matrix
		self.image = self.f[0][0]
		self.rect = self.image.get_rect()
		self.direction = 0
		self.action = 0
		self.index = 0
		self.rect.y = 50
		self.rect.x = 250

	def update(self, posMarioX, posMarioY):
		print "Delta x: ", abs(posMarioX - self.rect.x)
		print "Delta Y: ", abs(posMarioY - self.rect.y)
		if abs(posMarioY - self.rect.y) > abs(posMarioX - self.rect.x):
			if (posMarioX - self.rect.x < 0):
				self.direction = 2
				self.action = 2
			elif (posMarioX - self.rect.x > 0):
				self.direction = 1
				self.action = 2
			elif (posMarioX == self.rect.x) and (posMarioY - self.rect.y < 0):
			 	self.direction = 3
				self.action = 2
			elif (posMarioX == self.rect.x) and (posMarioY - self.rect.y < 0):
				self.direction = 4
				self.action = 2
		elif abs(posMarioY - self.rect.y) < abs(posMarioX - self.rect.x):
			if (posMarioY - self.rect.y < 0):
				self.direction = 3
				self.action = 2
			elif (posMarioY - self.rect.y > 0):
				self.direction = 4
				self.action = 2
			elif (posMarioY == self.rect.y) and (posMarioX - self.rect.x < 0):
				self.direction = 2
				self.action = 2
			elif (posMarioY == self.rect.y) and (posMarioX - self.rect.x > 0):
				self.direction = 1
				self.action = 2
		else:
			self.action = 1

		if self.direction == 1 and self.action == 2:
			self.image = self.f[0][self.index]
			self.index += 1
			if self.rect.x <= width - 150:
				self.rect.x += 5
			if self.index >= 15:
				self.index = 0
		elif self.direction == 2 and self.action == 2:
			self.image = self.f[1][self.index]
			self.index += 1
			if self.rect.x >= 20:
				self.rect.x -= 5
			if self.index >= 15:
				self.index = 0
		elif self.direction == 3 and self.action == 2:
			self.image = self.f[3][self.index]
			self.index += 1
			if self.index >= 15:
				self.index = 0
			if self.rect.y >= 40:
				self.rect.y -= 5
		elif self.direction == 4 and self.action == 2:
			self.image = self.f[2][self.index]
			self.index += 1
			if self.index >= 15:
				self.index = 0
			if self.rect.y <= height - 80:
				self.rect.y += 5


		if self.action == 1:
			if self.direction == 2:
				self.image = self.f[5][self.index]
			else:
				self.image = self.f[4][self.index]
			self.index +=1
			if self.index >=16:
				self.index = 0
				if self.direction == 2:
					self.image = self.f[1][self.index]
				else:
					self.image = self.f[0][self.index]
				self.action = 0

def generateAmbient():
	pantalla.blit(imageFondo, [posx, posy])


#generar menu

def menuStart(colorUno,colorDos,a,b):
	pantalla.fill(BLANCO)
	fondo = pygame.image.load("source/fondoMenu.png")
	pantalla.blit(fondo,[0,0])
	largoTexto = pygame.font.Font('freesansbold.ttf',a)
	largoTextoDos = pygame.font.Font('freesansbold.ttf',b)
	renderUno = largoTexto.render("Jugar",True,colorUno)
	renderDos = largoTextoDos.render("Salir",True,colorDos)
	pos_Uno = (width/2,height/2)
	pos_Dos = (width/2,(height/2) + 35)
	pantalla.blit(renderUno,pos_Uno)
	pantalla.blit(renderDos,pos_Dos)
	pygame.display.flip()


#Recortar sprite
def recortarSprite(nombrearchivo, cantidadX, cantidadY):
	imageSprite = pygame.image.load(nombrearchivo)
	imageInfo = imageSprite.get_rect()
	imageWidth = imageInfo[2]
	imageHeight = imageInfo[3]
	if nombrearchivo == 'source/mariofinal.png' or nombrearchivo == 'source/luigifinal.png':
		corteX = 33
	else:
		corteX = (imageWidth / cantidadX)
	matrix = []
	corteY = (imageHeight / cantidadY)
	listaCorte = [8,8,8,8,9,9,6,6]
	for y in range(cantidadY):
		matrix.append([])
		for x in range(cantidadX):
			cuadro = imageSprite.subsurface(corteX * x, corteY * y, corteX,corteY)
			matrix[y].append(cuadro)
	return matrix

def saludPersonajes(saludMario,saludLuigi):
    pantalla.fill([0,0,0])
    if saludMario>=0:
        saludMario -= 1
        pygame.draw.line(pantalla,[0,255,0],[0,10],[100,10],50)
        pygame.draw.line(pantalla,[255,0,0],[100 - saludMario,10],[100,10],50)
    if saludLuigi>=0:
        saludLuigi -= 1
        pygame.draw.line(pantalla,[0,255,0],[width-100,10],[width,10],50)
        pygame.draw.line(pantalla,[255,0,0],[width-saludLuigi,10],[width,10],50)

def dibujarBarraSalud():
	  #salud Mario
    pygame.draw.line(pantalla,[0,255,0],[0,10],[100,10],50)
    pygame.draw.line(pantalla,[255,0,0],[100,10],[100,10],50)
    #salud luigi
    pygame.draw.line(pantalla,[0,255,0],[width-100,10],[width,10],50)
    pygame.draw.line(pantalla,[255,0,0],[width,10],[width,10],50)
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    readerFileCollide()
    imageFondo = pygame.image.load('source/fondo.png')
    imagefondoInfo = imageFondo.get_rect()
    imageFondoWidth = imagefondoInfo[2]
    imageFondoHeight = imagefondoInfo[3]
    generateAmbient()
    matrixMario = recortarSprite('source/mariofinal.png', 14, 12)
    jugador = Jugador(matrixMario,10,40)
    jugadores.add(jugador)
    todos.add(jugador)
    matrixLuigi = recortarSprite('source/luigifinal.png',14,12)
    jugadorDos = Jugador(matrixLuigi,1,40)
    jugadores.add(jugadorDos)
    todos.add(jugadorDos)
    matrixBowser = recortarSprite('source/Bowser.png', 17, 6)
    bowser = BowserEnemy(matrixBowser)
    enemigosBowser.add(bowser)
    todos.add(bowser)
    pygame.display.flip()
    selection = False
    menuPos = 1
    a=20
    b=20
    menuStart(ROJO,NEGRO,a*2,b)
    done = False
    while not selection:

    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
				done = True
				selection = True
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_DOWN:
    				menuPos +=1
    				if menuPos == 2:
    					b = b*2
    					a=20
    					menuStart(NEGRO,ROJO,a,b)
    				elif menuPos >= 2:
    					menuPos = 2
    			elif event.key == pygame.K_UP:
    				menuPos -=1
    				if menuPos == 1:
    					a = a*2
    					b=20
    					menuStart(ROJO,NEGRO,a,b)
    				elif menuPos <= 0:
    					menuPos = 1

    			elif event.key == pygame.K_SPACE:
    				if menuPos == 1:
    					selection = True
    				elif menuPos == 2:
    					done = True
    					selection = True
    
    fondo.play()
    while not done:
        for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			elif event.type == pygame.KEYDOWN:
				jugador.index = 0
				if event.key == pygame.K_RIGHT:
					jugador.direction = 1
					jugador.action = 2
				elif event.key == pygame.K_l:
					jugador.direction = 2
					jugador.action = 2
				elif event.key == pygame.K_UP:
					jugador.direction = 3
					jugador.action = 2
				elif event.key == pygame.K_b:
					jugador.direction = 4
					jugador.action = 2
				elif event.key == pygame.K_d:
					jugadorDos.direction = 1
					jugadorDos.action = 2
				elif event.key == pygame.K_a:
					jugadorDos.direction = 2
					jugadorDos.action = 2
				elif event.key == pygame.K_w:
					jugadorDos.direction = 3
					jugadorDos.action = 2
				elif event.key == pygame.K_s:
					jugadorDos.direction = 4
					jugadorDos.action = 2
				elif event.key == pygame.K_SPACE:
					jugador.direction = 0
				elif event.key == pygame.K_p:
					golpe.play()
					jugador.action = 1
				elif event.key == pygame.K_m:
					jugador.action = 3

        if jugador.direction == 1 and jugador.action == 2 and jugador.rect.x >= width -150 and posx >= width - imageFondoWidth:
        	if validateMove(int(ceil((jugador.rect.x + abs(posx) + 30) / 32)), int(ceil((jugador.rect.y + abs(posy) + 20) / 32))):
        		posx -= 5
        elif jugador.direction == 2 and jugador.action == 2 and jugador.rect.x <= 20 and posx <= -10:
        	if validateMove(int(ceil((jugador.rect.x + abs(posx)) / 32)), int(ceil((jugador.rect.y + abs(posy) + 20) / 32))):
        		posx += 5
        elif jugador.direction == 3 and jugador.action == 2 and jugador.rect.y <= 40 and posy <= -10:
        	if validateMove(int(ceil((jugador.rect.x + abs(posx) + 16) / 32)), int(ceil((jugador.rect.y + abs(posy) + 16) / 32))):
        		posy += 5
        elif jugador.direction == 4 and jugador.action == 2 and jugador.rect.y >= height - 80 and posy >= height- imageFondoHeight:
        	if validateMove(int(ceil((jugador.rect.x + abs(posx) + 16) / 32)), int(ceil((jugador.rect.y + abs(posy) + 32) / 32))):
        		posy -= 5
        dibujarBarraSalud()
        generateAmbient()
        dibujarBarraSalud()
    	todos.draw(pantalla)
    	jugadores.update()
    	enemigosBowser.update(jugador.rect.x, jugador.rect.y)
    	pygame.display.flip()
    	reloj.tick(10)
