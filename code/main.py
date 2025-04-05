from settings import *
from map import Map
from sprite import sprites, Sprite
from input import keys_down
from player import Player
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Yippee Enginneer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Map("tilemap.txt")

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    keys_down.add(event.key)
                elif event.type == pygame.KEYUP:
                    keys_down.remove(event.key)
            
            self.screen.fill((30, 150, 50))
            self.draw_map()
            Player.update()
            for sprite in sprites:
                sprite.draw(self.screen)
            pygame.display.flip()
    
    def draw_map(self):
        self.map.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()