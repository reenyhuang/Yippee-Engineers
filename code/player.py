import pygame
from sprite import Sprite
from input import is_key_pressed
from os import path
from settings import TILE_SIZE

movement_speed = TILE_SIZE
rotation_speed = 1

class Player(Sprite):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y)
        self.original_image = self.image
        self.angle = 0
        self.game = game
        self.rect = self.image.get_rect(center=(self.x, self.y))
        

    def bump_into_something(self, dx=0, dy=0):
        future_rect = self.rect.copy()
        future_rect.x += dx * TILE_SIZE
        future_rect.y += dy * TILE_SIZE
        for wall in self.game.walls:
            if future_rect.colliderect(wall.rect):
                return True
        return False

    def move(self, dx=0, dy=0):
        
        new_x = self.x + dx*movement_speed
        new_y = self.y + dy*movement_speed

        future_rect = self.rect.copy()
        future_rect.x = new_x
        future_rect.y = new_y

        if not any(future_rect.colliderect(wall.rect) for wall in self.game.walls):
            self.x = new_x
            self.y = new_y
            self.rect.topleft = (self.x, self.y)

        #if dx != 0 or dy != 0: ## Pretty sure this if statement is not necessary, the direction checks same thing
        direction = dx if dx != 0 else dy
        self.angle += rotation_speed * direction

        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect.x, self.rect.y = self.x * TILE_SIZE, self.y * TILE_SIZE

        #else:
            #self.image = self.original_image
            #self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        self.move()
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE


        





