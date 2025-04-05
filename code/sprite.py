import pygame
from os import path
sprites = []
loaded = {}

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, *groups):
        super().__init__(*groups)
        folder = path.dirname(__file__)
        image = path.join(folder, image)
        if image in loaded:
            self.image = loaded[image]
        else:
            self.image = pygame.image.load(image).convert_alpha()
            loaded[image] = self.image
        self.x = x
        self.y = y
        
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.05, self.image.get_height() * 0.05))

    #def delete(self):
    #    sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))