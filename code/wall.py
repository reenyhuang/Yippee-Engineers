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
        image = path.join(folder, "images", "balcony_h.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
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
        image = path.join(folder, "images", "balcony_v.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
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
        image = path.join(folder, "images", "balcony_j.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE - 15
        self.rect.y = y * TILE_SIZE

class BalconyK(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "balcony_k.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE - 15

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
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
        self.rect.x = x * TILE_SIZE - 20
        self.rect.y = y * TILE_SIZE - 20


class Elevator(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.elevators
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "black_tile.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE - 25
        self.rect.y = y * TILE_SIZE - 28

class Carpet(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "carpet.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE + 15
        self.rect.y = y * TILE_SIZE + 13
    

class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "grass.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE - 15
        self.rect.y = y * TILE_SIZE - 9

class Door(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "black_tile.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE - 25
        self.rect.y = y * TILE_SIZE - 28

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
        self.rect.x = x * TILE_SIZE - 11
        self.rect.y = y * TILE_SIZE - 29

class Club(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.club
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
        self.rect.x = x * TILE_SIZE - 11
        self.rect.y = y * TILE_SIZE - 29

class Test(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.test
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "test.png")
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
        self.rect.x = x * TILE_SIZE -11
        self.rect.y = y * TILE_SIZE -29

class VendingMachine(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.vending
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "vending_machine.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.05, self.image.get_height() * 0.05))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE + 12
        self.rect.y = y * TILE_SIZE

class Advisor(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.advisor
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        folder = path.dirname(__file__)
        folder = path.dirname(folder)
        image = path.join(folder, "images", "advisor.png")
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE -25
        self.rect.y = y * TILE_SIZE -20


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
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.1, self.image.get_height() * 0.1))
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
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE -61
        self.rect.y = y * TILE_SIZE -21

class Study(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.study
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