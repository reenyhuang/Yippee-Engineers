from settings import *
from map import Map
from wall import Wall
from sprite import sprites, Sprite
from input import keys_down
from player import Player
import pygame

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
        self.map = Map("tilemap.txt")
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tile in enumerate(self.map.map_data):
            for col, tile_type in enumerate(tile):
                if tile_type == '1':
                    Wall(self, row, col)
        
        
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player("RoundLili.png", 0, 0, self)
        for x in range(10, 20):
            Wall(self, x, 5)

    def run(self):
        while self.running:
            self.events() ## Handle events
            self.draw_map() ## Draw the background map
            self.update() ## Draw all sprites and update them
            
            pygame.display.flip() ## Update screen
            
    
    def update(self):
        self.player.update()
        self.all_sprites.draw(self.screen) ## Draw all sprites
        for sprite in sprites: ## Also draw all sprites? I think we're keeping track of some sprites in two different places
            sprite.draw(self.screen)

    def events(self): ## Key press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key in forward_keys:
                    self.player.move(dy=-1)
                elif event.key in backward_keys:
                    self.player.move(dy=1)
                elif event.key in left_keys:
                    self.player.move(dx=-1)
                elif event.key in right_keys:
                    self.player.move(dx=1)
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                pass
            

    def draw_map(self):
        self.screen.fill(BG_COLOR)
        self.map.draw(self.screen)
    
    def quit(self):
        pygame.quit()
        exit()
    




if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()