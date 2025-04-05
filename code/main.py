from settings import *
from map import Map, Camera
from wall import Wall, Elevator
from sprite import sprites, Sprite
from input import keys_down
from player import Player
from healthBar import HealthBar
from inventory import Inventory
import pygame
from os import path
from random import randint
BG_COLOR = (222, 235, 255)
import time

pygame.font.init()
font = pygame.font.Font(None, 36)


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.key.set_repeat(1000, 100)
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Yippee Enginneer")
        self.clock = pygame.time.Clock()
        self.clock.tick(60)
        self.start_time = time.time()
        self.curr_time = time.time()
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
        #self.inv = Inventory()
        self.custom_event = True


    def get_time(self):
        '''Elapsed time in seconds.'''
        self.curr_time = time.time()
        elapsed_time = self.curr_time - self.start_time
        elapsed_time = int(elapsed_time)
        return elapsed_time
    
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

    def get_clock_time(self):
        '''Return string of in game time: hours:minutes. 6 hr clock, 1 min = 1 sec.'''
        elapsed_time = self.get_time()
        hours = (elapsed_time // 60) % 6
        minutes = elapsed_time % 60
        return f"{hours}:{minutes:02d}"

    def run(self):
        while self.running:
            
            if self.get_clock_time() == "1:00" and self.custom_event:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: randint(0, 5)}))
                self.custom_event = False
            if self.get_clock_time() == "2:00":
                self.custom_event = True
            self.events() ## Handle events
            self.draw() ## Draw the background map
            self.update() ## Draw all sprites and update them
            self.healthbar.hp = 70
            self.screen.blit(font.render(self.get_clock_time(), True, (0, 0, 0), (255, 255, 255)), (1200, 10))
            pygame.display.flip() ## Update screen
            
    
    def draw(self):
        self.draw_map()
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.healthbar.draw(self.screen)
        #self.inventory.render(self.screen)

    def inventory(self):
        pass

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
            elif event.type == pygame.USEREVENT:
                event_id = event.dict[id]
                if event_id == 0:
                    pass ## Random events
                elif event_id == 1:
                    pass
                elif event_id == 2:
                    pass
                elif event_id == 3:
                    pass
                elif event_id == 4:
                    pass
                elif event_id == 5:
                    pass
            
    
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