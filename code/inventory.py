import pygame
from inventorySlot import InventorySlot

class Inventory:
    def __init__(self):
        self.slots = []

        self.image = pygame.image.load("images/inventory.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 160)

        self.slots.append(InventorySlot("images/coffee.png", (16, 176)))
        self.slots.append(InventorySlot("images/computer.png", (16, 257)))
        self.slots.append(InventorySlot("images/hw.png", (16, 335)))
        self.slots.append(InventorySlot("images/charger.png", (16, 415)))
        self.slots[1].count += 1
        self.slots[3].count += 1
    
    def render(self, display):
        display.blit(self.image, self.rect)
        for slot in self.slots:
            slot.render(display)