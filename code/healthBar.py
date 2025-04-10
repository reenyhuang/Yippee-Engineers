from settings import *
import pygame

class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = 70
        self.max_hp = max_hp

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))

    def decrease(self, num):
        if (self.hp-num) >= 0:
            self.hp -= num
        else:
            self.hp = 0

    def increase(self, num):
        if (self.hp+num) <= self.max_hp:
            self.hp += num
        else:
            self.hp = 100
