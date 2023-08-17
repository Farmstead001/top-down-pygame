import pygame
from settings import *

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = win_height / 2
        self.y = win_width / 2

        self.speed = 0.5
        self.dash = 3

        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)

    def draw(self):
        pygame.draw.rect(self.screen, player_color, (self.x, self.y, player_width, player_height))

    def get_input(self):

        # D-pad
        if self.controller.get_button(11): # D-pad up
            self.y -= self.speed
        if self.controller.get_button(12): # D-pad down
            self.y += self.speed
        if self.controller.get_button(13): # D-pad left
            self.x -= self.speed
        if self.controller.get_button(14): # D-pad right
            self.x += self.speed

        # stick
        if self.controller.get_axis(1): # up => down
            self.y += self.controller.get_axis(1) * self.speed
        if self.controller.get_axis(0): # right => left
            self.x += self.controller.get_axis(0) * self.speed

    def update(self):
        self.get_input()
        self.draw()