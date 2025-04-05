from settings import *
from map import Map, Camera
from wall import Wall
from sprite import sprites, Sprite
from input import keys_down
from player import Player
import pygame
from os import path

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

BG_COLOR = (222, 235, 255)

forward_keys = (pygame.K_UP, pygame.K_w)
backward_keys = (pygame.K_DOWN, pygame.K_s)
left_keys = (pygame.K_LEFT, pygame.K_a)
right_keys = (pygame.K_RIGHT, pygame.K_d)

class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(500, 100)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Yippee Enginneer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.maps = []
        self.curr_map = None
        self.camera = None
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = None
    
    def new(self):
        self.maps = [Map("floorG.txt"), Map("floor1.txt"), Map("floor2.txt")]
        self.curr_map = self.maps[0]
        self.camera = Camera(self.curr_map.width, self.curr_map.height)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        
        for row, tiles in enumerate(self.curr_map.map_data):
            for col, tile_type in enumerate(tiles):
                if tile_type == '1':
                    Wall(self, col, row)
                elif tile_type == 'P':
                    self.player = Player("RoundLili.png", col, row, self)


    def run(self):
        while self.running:
            self.events() ## Handle events
            self.draw() ## Draw the background map
            self.update() ## Draw all sprites and update them
            
            
            pygame.display.flip() ## Update screen
            
    
    def draw(self):
        self.draw_map()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

    def update(self):
        self.player.update()
        self.camera.update(self.player)

    def events(self): ## Key press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                keys_down.add(event.key)
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                keys_down.remove(event.key)
            

    def draw_map(self):
        self.screen.fill(BG_COLOR)
        self.curr_map.draw(self.screen)
    
    def quit(self):
        pygame.quit()
        exit()
    




if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()