import pygame
from pygame import _sdl2

from settings import *
from player import Player


# pygame init
background_colour = (0, 0, 0)
screen = pygame.display.set_mode((win_height, win_width))
pygame.display.set_caption('prototype #1')

pygame.display.flip()
running = True

# player init
player = Player(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_colour)
    
    player.update()

    pygame.display.flip()
