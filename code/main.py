from settings import *
from map import Map, Wall
from sprite import sprites, Sprite
from input import keys_down
from player import Player
import pygame

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500, 800)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Yippee Enginneer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.map = Map("tilemap.txt")
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tile in enumerate(self.map.map_data):
            for col, tile_type in enumerate(tile):
                if tile_type == '1':
                    Wall(self, row, col)
        self.player = Player("RoundLili.png", 0, 0)

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
            self.player.update()
            for sprite in sprites:
                sprite.draw(self.screen)
            pygame.display.flip()
    
    def draw_map(self):
        self.map.draw(self.screen)

if __name__ == '__main__':
    game = Game()
    game.run()