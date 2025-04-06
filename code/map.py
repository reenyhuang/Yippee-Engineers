import pygame
from pygame.locals import *
from os import path
from wall import Wall

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 32

GRID_COLOR = (155, 158, 163)

## Tilemap txt doc format:
## . = empty
## G = grass
## 1 = wall
## P = spawn point
## E = Elevator
## B = Couch (bed)
## C = Carpet
## T = Tile
## t = Table
## c = Classroom
## A = Advisor
## S = Starbucks
## R = vert balcony
## H = horiz balcony
## J = corner balcony
## K = corner balcony
## Character currently 4 tiles wide
## Make everything very large


class Map:
    def __init__(self, filename):
        self.map_data = []
        folder = path.dirname(__file__)
        filename = path.join(folder, filename)
        with open(filename, 'r') as f:
            for line in f:
                self.map_data.append(line.strip())
        self.tile_width = len(self.map_data[0])
        self.tile_height = len(self.map_data)
        self.width = self.tile_width * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

    def draw(self, screen):
        # Draw the grid
        for x in range(0, WINDOW_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))
        

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        x = -target.rect.x + int(WINDOW_WIDTH/2)
        y = -target.rect.y + int(WINDOW_HEIGHT/2)
        x = min(0, x)
        x = max(-(self.width - WINDOW_WIDTH), x)
        y = min(0, y)
        y = max(-(self.height - WINDOW_HEIGHT), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)