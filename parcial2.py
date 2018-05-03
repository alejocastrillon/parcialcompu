# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alejandro"
__date__ = "$2/05/2018 08:18:46 PM$"

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
