import pygame
from inventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("Images/Inventory.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 350)