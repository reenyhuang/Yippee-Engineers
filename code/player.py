import pygame
from sprite import Sprite
from input import is_key_pressed
from os import path
from settings import TILE_SIZE

movement_speed = .5
rotation_speed = 1



class Player(Sprite):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y)
        self.original_image = self.image
        self.angle = 0
        self.game = game
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.rect = self.image.get_rect()
        

    def move(self):
        forward_pressed = is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w)
        backward_pressed = is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s)
        left_pressed = is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a)
        right_pressed = is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d)
        dx, dy = 0, 0
        if forward_pressed:
            dy -= movement_speed
        elif backward_pressed:
            dy += movement_speed
        if left_pressed:
            dx -= movement_speed
        elif right_pressed:
            dx += movement_speed

        future_rect = self.rect.copy()
        future_rect.topleft = (round(self.x + dx), round(self.y + dy))
        

        if not any(future_rect.colliderect(wall.rect) for wall in self.game.walls):
            self.x += dx
            self.y += dy
            self.rect.topleft = (round(self.x), round(self.y))

        
        direction = dx if dx != 0 else dy
        self.angle += rotation_speed * direction

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        

        

    def update(self):
        self.move()


        





