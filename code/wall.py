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
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "brick_wall_horiz.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.65, self.image.get_height() * 0.68))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class BalconyH(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "brick_wall_horiz.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.65, self.image.get_height() * 0.68))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class BalconyV(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "brick_wall_horiz.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.65, self.image.get_height() * 0.68))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class BalconyJ(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "brick_wall_horiz.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.65, self.image.get_height() * 0.68))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE

class BalconyK(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "brick_wall_horiz.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.65, self.image.get_height() * 0.68))
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
    


class Classroom(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.classroom
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "red_tile.png")
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

class Friends(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.friends
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "red_tile.png")
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

class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.grass
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "red_tile.png")
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

class Coffee(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coffee
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "coffee.png")
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

class Movie(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.movie
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "movie.png")
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

class Sleep(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.sleep
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "couch.png")
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