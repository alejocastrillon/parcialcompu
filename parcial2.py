import pygame

size = width, height = [680, 400]
if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode(size)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
