import pygame
from sprite import Sprite
from input import is_key_pressed

movement_speed = 2

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

    def update(self):
        forward = pygame.K_UP or pygame.K_w
        backward = pygame.K_DOWN or pygame.K_s
        left = pygame.K_LEFT or pygame.K_a
        right = pygame.K_RIGHT or pygame.K_d
        if is_key_pressed(forward):
            self.y -= movement_speed
        if is_key_pressed(backward):
            self.y += movement_speed
        if is_key_pressed(left):
            self.x -= movement_speed
        if is_key_pressed(right):
            self.x += movement_speed