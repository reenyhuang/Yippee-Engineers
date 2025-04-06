from settings import *
from map import Map, Camera
from wall import *
from sprite import sprites, Sprite
from input import keys_down
from player import Player, Lili
from healthBar import HealthBar
from inventory import Inventory
from button import Button
import sys
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
        self.classroom = pygame.sprite.Group()
        self.friends = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()
        self.coffee = pygame.sprite.Group()
        self.movie = pygame.sprite.Group()
        self.sleep = pygame.sprite.Group()
        self.pet = pygame.sprite.Group()
        self.test = pygame.sprite.Group()
        self.balcony = pygame.sprite.Group()
        self.study = pygame.sprite.Group()
        self.club = pygame.sprite.Group()
        self.vending = pygame.sprite.Group()
        self.advisor = pygame.sprite.Group()
        
        self.elev_timer = 0
        self.club_timer = 0
        self.lili_timer = 0
        self.test_timer = 0
        self.coffee_timer = 0
        self.coffee1_timer = 0
        self.movie_timer = 0
        self.friends_timer = 0
        self.class_timer = 0
        self.balcony_timer = 0
        self.walk_timer = 0
        self.study_timer = 0
        self.sleep_timer = 0
        self.food_timer = 0
        self.piz_timer = 0
        
        self.player = None
        self.lili = None
        self.healthbar = HealthBar(390, 650, 500, 40, 100)
        self.inv = Inventory()
        self.custom_event = True
        self.piz = 0
        self.edu = 0


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
        
        player_location = (0, 0)
        for row, tiles in enumerate(self.curr_map.map_data):
            for col, tile_type in enumerate(tiles):
                if tile_type == '1':
                    Wall(self, col, row)
                elif tile_type == 'P':
                    Tile(self, col, row)
                    player_location = (col, row)
                elif tile_type == 'E':
                    Elevator(self, col, row)
                elif tile_type == 'H':
                    BalconyH(self, col, row)
                elif tile_type == 'R':
                    BalconyV(self, col, row)
                elif tile_type == 'J':
                    BalconyJ(self, col, row)
                elif tile_type == 'K':
                    BalconyK(self, col, row)
                elif tile_type == 'T':
                    Tile(self, col, row)
                elif tile_type == 'C':
                    Carpet(self, col, row)
                elif tile_type == 'c':
                    Classroom(self, col, row)
                elif tile_type == 'G':
                    Grass(self, col, row)
                elif tile_type == 'D':
                    Door(self, col, row)
                elif tile_type == 'S':
                    Sleep(self, col, row)
                elif tile_type == 's':
                    Coffee(self, col, row)
                elif tile_type == 'V':
                    VendingMachine(self, col, row)
                elif tile_type == 'A':
                    Advisor(self, col, row)

                
        
        self.lili = Lili("RoundLili.png", 12, 12, self)
        self.player = Player("RoundLili.png", player_location[0], player_location[1], self)

    def get_clock_time(self):
        '''Return string of in game time: hours:minutes. 6 hr clock, 1 min = 1 sec.'''
        elapsed_time = self.get_time()
        hours = (elapsed_time // 60) % 6
        minutes = elapsed_time % 60
        return f"{hours}:{minutes:02d}"

    def run(self):
        self.menu()
        self.start_time = time.time()
        self.running = True
        while self.running:
            #have a beginning scene
            if (self.get_clock_time() == "1:00" or self.get_clock_time() == "4:00") and self.custom_event:
                pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: randint(0, 5)}))
                self.custom_event = False
            if (self.get_clock_time() == "2:00" or self.get_clock_time() == "3:00") and self.custom_event:
                self.alert("Go to Class: G415")
                self.custom_event = False
            if self.get_clock_time() == "1:01" or self.get_clock_time() == "4:01":
                self.custom_event = True
            if self.get_clock_time() == "0:00" and self.custom_event:
                self.inv.slots[2].count += 2
                self.custom_event = False
            if self.get_clock_time() == "0:01":
                self.custom_event = True
            if self.healthbar.hp <= 0:
                self.screen_cap("images/jump.png", "You Died :(")
                self.quit()
            self.events(self.healthbar) ## Handle events
            self.draw() ## Draw the background map
            self.update() ## Draw all sprites and update them
            self.screen.blit(font.render(self.get_clock_time(), True, (0, 0, 0), (255, 255, 255)), (1200, 10))
            pygame.display.flip() ## Update screen
            
    def screen_cap(self, img, msg, font_size = 48, text_color=(255, 0, 0)):
        img1 = pygame.image.load(img).convert_alpha()
        imgt = pygame.transform.scale(img1, (WINDOW_WIDTH, WINDOW_HEIGHT))
        self.screen.blit(imgt, (0,0))
        font = pygame.font.Font(None, font_size)
        text = font.render(msg, True, text_color)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(2000)

    def alert(self, msg):
        popup_width, popup_height = 400, 200
        popup = pygame.Surface((popup_width, popup_height))
        popup.fill((240, 240, 240))  # Light gray background
        popup_rect = popup.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        text = font.render(msg, True, (0, 0, 0))
        text_rect = text.get_rect(center=(popup_width // 2, 60))
        popup.blit(text, text_rect)

        button_color = (200, 50, 50)
        button_rect = pygame.Rect(popup_width // 2 - 50, 130, 100, 40)
        pygame.draw.rect(popup, button_color, button_rect)
        button_text = font.render("OK", True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        popup.blit(button_text, button_text_rect)

        self.screen.blit(popup, popup_rect)
        pygame.display.update()    
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if button_rect.move(popup_rect.left, popup_rect.top).collidepoint(mouse_pos):
                        waiting = False


    def draw(self):
        self.draw_map()
        
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.healthbar.draw(self.screen)
        self.inv.render(self.screen)

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
                    self.screen_cap("images/angry_professor.png", "Haunted by Professor: -60% HP")
                    hb.decrease(hb.max_hp*.6)
                elif event_id == 1: # power outage
                    self.screen_cap("images/blackout.png", "Power Outage: +10% HP (yayyyyyy)")
                    hb.increase(hb.max_hp*.1)
                elif event_id == 2: # lose charger
                    self.screen_cap("images/lose_charger.png", "Oh NOOOO, donde esta?: -50% HP")
                    hb.decrease(hb.max_hp*.5)
                elif event_id == 3: # cry
                    self.screen_cap("images/crying.png", "DYIIINNGGGGG: -30% HP")
                    hb.decrease(hb.max_hp*.3)
                elif event_id == 4: #computer dies
                    self.screen_cap("images/computer_dies.png", "FCK: -40% HP")
                    hb.decrease(hb.max_hp*.4)
                elif event_id == 5: #have a test
                    hb.decrease(hb.max_hp*.5 * min(self.edu, 5))
                elif event_id == 6: #starvation/dehydation
                    hb.decrease(hb.max_hp*.1)
                    self.alert("Starving! -10% HP")
                elif event_id == 7: #study (less than 3 hrs)
                    hb.increase(hb.max_hp*.05)
                elif event_id == 8: #study more than 3 hrs
                    hb.decrease(hb.max_hp*.4)
                elif event_id == 9: #drink coffee
                    hb.increase(hb.max_hp*.1)
                elif event_id == 10: #hang with friends
                    hb.increase(hb.max_hp*.3)
                elif event_id == 11: #sleep in esc office
                    if randint(0, 9):
                        hb.increase(hb.max_hp*.2)
                    else:
                        hb.hp = 0
                elif event_id == 12: #go to balcony
                    hb.increase(hb.max_hp*.1)
                elif event_id == 13: #go to club meeeting
                    hb.increase(hb.max_hp*.05)
                elif event_id == 14: #watch la la land
                    hb.increase(hb.max_hp*.3)
                elif event_id == 15: #pet lili
                    hb.increase(hb.max_hp*.01)
                elif event_id == 16: #mental health walk
                    hb.increase(hb.max_hp*.15)
                elif event_id == 17: #go to class
                    hb.decrease(hb.max_hp*.03)
                    self.alert("Attending Class for 1 Hour")
                    pygame.time.wait(10000)
                elif event_id == 18: #do hw
                    hb.decrease(hb.max_hp*.1)
                elif event_id == 19: #eat pizza
                    hb.increase(hb.max_hp*.03)
            
    
    def draw_map(self):
        self.screen.fill(BG_COLOR)
        #self.curr_map.draw(self.screen)
    
    def change_floor(self, floor=1):
        self.curr_map = self.maps[floor % len(self.maps)]
        self.camera = Camera(self.curr_map.width, self.curr_map.height)
        self.all_sprites.empty()
        self.walls.empty()
        self.elevators.empty()
        self.classroom.empty()
        self.friends.empty()
        spawn_x, spawn_y = self.load_map()
        
        self.player = Player("RoundLili.png", spawn_x, spawn_y, self)

    def load_map(self):
        spawn_x, spawn_y = 0, 0
        need_spawn = True
        for row, tiles in enumerate(self.curr_map.map_data):
            for col, tile_type in enumerate(tiles):
                if tile_type == '1':
                    Wall(self, col, row)
                elif tile_type == 'E':
                    Elevator(self, col, row)
                    if need_spawn:
                        spawn_x, spawn_y = col, row
                        need_spawn = False
                elif tile_type == 'H':
                    BalconyH(self, col, row)
                elif tile_type == 'R':
                    BalconyV(self, col, row)
                elif tile_type == 'J':
                    BalconyJ(self, col, row)
                elif tile_type == 'K':
                    BalconyK(self, col, row)
                elif tile_type == 'P':
                    Tile(self, col, row)
                elif tile_type == 'T':
                    Tile(self, col, row)
                elif tile_type == 'C':
                    Carpet(self, col, row)
                elif tile_type == 'c':
                    Classroom(self, col, row)
                elif tile_type == 'G':
                    Grass(self, col, row)
                elif tile_type == 'D':
                    Door(self, col, row)
                elif tile_type == 'S':
                    Sleep(self, col, row)
                elif tile_type == 's':
                    Coffee(self, col, row)
                elif tile_type == 'V':
                    VendingMachine(self, col, row)
                elif tile_type == 'A':
                    Advisor(self, col, row)
        ## Put Lili on random floors
        if randint(0, 1):
            self.lili = Lili("RoundLili.png", 8, 10, self)

        return spawn_x, spawn_y

    def quit(self):
        pygame.quit()
        exit()
    
    def help(self):
        while self.running:
            help_mouse = pygame.mouse.get_pos()
            self.screen.fill("white")
            posX = 640
            posY = 260
            position = posX, posY
            temptxt = ["So you're new here then?", 
                       "Use WASD or arrow keys to move", 
                       "Press space to drink coffee", 
                       "Using the elevator: E for up, Q for down",
                       "HW decreases mental health over time as it accumulates",
                       "Pay attention to your health bar at the bottom. DON'T DIE!",
                       "You can pet Lili the cat with L",
                       "Press E to interact, try it in various spaces around engineering and in classrooms/studyrooms",
                       "An average day for your avatar is 6 hours, 6 minutes in real time"]
            label = []
            for line in temptxt:
                label.append(font.render(line, True, "Black"))
            for line in range(len(label)):
                help_rect = label[line].get_rect(center=(position[0], position[1]))
                posY += 20
                position = posX, posY
                self.screen.blit(label[line], help_rect)
                

            help_bck = Button(image=None, pos=(640, 460), 
                                text_input="BACK", font=pygame.font.Font(None, 75), base_color="Black", hovering_color="Green")

            help_bck.changeColor(help_mouse)
            help_bck.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if help_bck.checkForInput(help_mouse):
                        self.run()

            pygame.display.update()

    
    def menu(self):
        while self.running:
            self.screen.fill("white")
            mouse = pygame.mouse.get_pos()
            txt = pygame.font.Font(None, 100).render("Main Menu", True, "#b68f40")
            rect = txt.get_rect(center=(640, 100))
            play_im = pygame.image.load("images/start_button.png").convert_alpha()
            play_imt = pygame.transform.scale(play_im, (play_im.get_width()*.80, play_im.get_height()*.80))
            help_im = pygame.image.load("images/help_button.png").convert_alpha()
            help_imt = pygame.transform.scale(help_im, (help_im.get_width()*.45, help_im.get_height()*.38))
            end_im = pygame.image.load("images/end_button.png")
            end_imt = pygame.transform.scale(end_im, (end_im.get_width()*.45, end_im.get_height()*.35))
            play_but = Button(image=play_imt, pos=(640, 250), text_input="", font=pygame.font.Font(None, 75), base_color="#d7fcd4", hovering_color="White")
            help_but = Button(image=help_imt, pos=(640, 400), text_input="", font=pygame.font.Font(None, 75), base_color="#d7fcd4", hovering_color="White")
            end_but = Button(image=end_imt, pos=(640, 550), text_input="", font=pygame.font.Font(None, 75), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(txt, rect)

            for button in [play_but, help_but, end_but]:
                button.changeColor(mouse)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_but.checkForInput(mouse):
                        self.running = False
                    if help_but.checkForInput(mouse):
                        self.help()
                    if end_but.checkForInput(mouse):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
        self.running=True

if __name__ == '__main__':
    game = Game()
    game.new()
    game.run()