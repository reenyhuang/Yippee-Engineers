import pygame
from pygame.locals import *
from settings import TILE_SIZE, WINDOW_HEIGHT, WINDOW_WIDTH


class Map:
    def __init__(self, filename):
        self.map_data = []
        with open(filename, 'r') as f:
            for line in f:
                self.map_data.append(line)
        self.tile_width = len(self.map_data[0])
        self.tile_height = len(self.map_data)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE
        

    def draw(self, screen):
        # Draw the grid
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, (255, 0, 0), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, (0, 255, 0), (0, y), (WINDOW_WIDTH, y))

