import pygame
from sprite import Sprite
from input import is_key_pressed
from os import path
from settings import TILE_SIZE

movement_speed = 1
rotation_speed = 1

class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.original_image = self.image
        self.angle = 0


    def update(self):
        dx, dy = 0, 0
        forward = pygame.K_UP or pygame.K_w
        backward = pygame.K_DOWN or pygame.K_s
        left = pygame.K_LEFT or pygame.K_a
        right = pygame.K_RIGHT or pygame.K_d
        if is_key_pressed(forward):
            dy -= movement_speed
        if is_key_pressed(backward):
            dy += movement_speed
        if is_key_pressed(left):
            dx -= movement_speed
        if is_key_pressed(right):
            dx += movement_speed

        self.x += dx
        self.y += dy

        if dx != 0 or dy != 0:
            direction = -1 if dx < 0 or dy < 0 else 1 if dx > 0 or dy > 0 else 0
            self.angle += rotation_speed * direction

            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=(self.x, self.y))

        else:
            self.image = self.original_image
            self.rect = self.image.get_rect(center=(self.x, self.y))





