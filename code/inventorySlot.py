import pygame

class InventorySlot:
    def __init__(self, name, pos):
        self.image = pygame.image.load(name).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.count = 0
        self.font = pygame.font.Font(None, 25)

    def render(self, display):
        text = self.font.render(str(self.count), True, (0,0,0))
        display.blit(self.image, self.rect)
        display.blit(text, self.rect.midright)