import pygame
from sprite import Sprite
from settings import TILE_SIZE
from os import path
loaded = {}

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((255, 204, 246))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class Elevator(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.elevators
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "gray_tile.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
    
