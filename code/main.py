from settings import *
from map import Map, Camera
from wall import Wall, Elevator
from sprite import sprites, Sprite
from input import keys_down
from player import Player
from healthBar import HealthBar
import pygame
from os import path
from random import randint
BG_COLOR = (222, 235, 255)



class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1000, 100)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Yippee Enginneer")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        
        self.running = True
        self.maps = []
        self.curr_map = None
        self.camera = None
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.elevators = pygame.sprite.Group()
        self.elev_timer = 0
        self.player = None
        self.lili = None
        self.healthbar = HealthBar(390, 650, 500, 40, 100)

    
    def new(self):
        self.maps = [Map("floorG.txt"), Map("floor1.txt"), Map("floor2.txt")]
        self.curr_map = self.maps[0]
        self.camera = Camera(self.curr_map.width, self.curr_map.height)
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.lili = Player("RoundLili.png", 8, 10, self)
        
        for row, tiles in enumerate(self.curr_map.map_data):
            for col, tile_type in enumerate(tiles):
                if tile_type == '1':
                    Wall(self, col, row)
                elif tile_type == 'P':
                    self.player = Player("RoundLili.png", col, row, self)
                elif tile_type == 'E':
                    Elevator(self, col, row)


    def run(self):
        while self.running:
            self.events() ## Handle events
            self.draw() ## Draw the background map
            self.update() ## Draw all sprites and update them
            self.healthbar.hp = 70
            
            pygame.display.flip() ## Update screen
            
    
    def draw(self):
        self.draw_map()
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.healthbar.draw(self.screen)

    def update(self):
        self.player.update()
        self.camera.update(self.player)
        self.lili.randomMov()
        self.clock.tick(80)

    def events(self): ## Key press events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                keys_down.add(event.key)
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key in keys_down:
                    keys_down.remove(event.key)
            
    
    def draw_map(self):
        self.screen.fill(BG_COLOR)
        #self.curr_map.draw(self.screen)
    
    def change_floor(self, floor=1):
        self.curr_map = self.maps[floor % len(self.maps)]
        self.camera = Camera(self.curr_map.width, self.curr_map.height)
        self.all_sprites.empty()
        self.walls.empty()
        self.elevators.empty()
        spawn_x, spawn_y = self.load_map()
        self.player = Player("RoundLili.png", spawn_x, spawn_y, self)

    def load_map(self):
        for row, tiles in enumerate(self.curr_map.map_data):
            for col, tile_type in enumerate(tiles):
                if tile_type == '1':
                    Wall(self, col, row)
                elif tile_type == 'E':
                    Elevator(self, col, row)
                    spawn_x, spawn_y = col, row
        ## If floor one
        if randint(0, 1):
            self.lili = Player("RoundLili.png", 8, 10, self)

        return spawn_x, spawn_y



    def quit(self):
        pygame.quit()
        exit()
    



if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()