from settings import *
from map import Map, Camera
from wall import Wall, Elevator
from sprite import sprites, Sprite
from input import keys_down
from player import Player
from healthBar import HealthBar
from inventory import Inventory
from button import Button
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
        self.inv = Inventory()
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
            if self.get_clock_time() == "0:00" and self.custom_event:
                self.inv.slots[2].count += 2
                self.custom_event = False
            if self.get_clock_time() == "0:01":
                self.custom_event = True
            self.events(self.healthbar) ## Handle events
            self.draw() ## Draw the background map
            self.update() ## Draw all sprites and update them
            self.screen.blit(font.render(self.get_clock_time(), True, (0, 0, 0), (255, 255, 255)), (1200, 10))
            pygame.display.flip() ## Update screen
            
    
    def draw(self):
        self.draw_map()
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.healthbar.draw(self.screen)
        self.inv.render(self.screen)

    def inventory(self):
        pass

    def update(self):
        self.player.update()
        self.camera.update(self.player)
        self.lili.randomMov()
        self.clock.tick(80)
        
    def events(self, hb): ## Key press events
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
                if event_id == 0: # haunted by professor
                    hb.decrease(hb.hp*.2)
                elif event_id == 1: # power outage
                    hb.increase(hb.hp*.1)
                elif event_id == 2: # lose charger
                    hb.decrease(hb.hp*.5)
                elif event_id == 3: # cry
                    hb.decrease(hb.hp*.2)
                elif event_id == 4: #computer dies
                    hb.decrease(hb.hp*.6)
                elif event_id == 5: #have a test
                    hb.decrease(hb.hp*.3)
                elif event_id == 6: #starvation/dehydation
                    hb.decrease(hb.hp*.1)
                elif event_id == 7: #study (less than 3 hrs)
                    hb.increase(hb.hp*.2)
                elif event_id == 8: #study more than 3 hrs
                    hb.decrease(hb.hp*.4)
                elif event_id == 9: #drink coffee
                    hb.increase(hb.hp*.2)
                elif event_id == 10: #hang with friends
                    hb.increase(hb.hp*.5)
                elif event_id == 11: #sleep in esc office
                    if randint(0, 9):
                        hb.increase(hb.hp*.3)
                    else:
                        hb.decrease(hb.hp*.6)
                elif event_id == 12: #go to balcony
                    hb.increase(hb.hp*.1)
                elif event_id == 13: #go to club meeeting
                    hb.increase(hb.hp*.05)
                elif event_id == 14: #watch la la land
                    hb.increase(hb.hp*.3)
                elif event_id == 15: #pet lili
                    hb.increase(hb.hp*.6)
                elif event_id == 16: #mental health walk
                    hb.increase(hb.hp*.3)
                elif event_id == 17: #go to class
                    hb.decrease(hb.hp*.2)
                elif event_id == 18: #do hw
                    hb.decrease(hb.hp*.1)
            
    
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
        ## Put Lili on random floors
        if randint(0, 1):
            self.lili = Player("RoundLili.png", 8, 10, self)

        return spawn_x, spawn_y

    def quit(self):
        pygame.quit()
        exit()
    
    def menu():
        mouse = pygame.mouse.get_pos()
        text = 


if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()