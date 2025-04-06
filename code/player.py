import pygame
import random
from sprite import Sprite
from input import is_key_pressed, keys_down
from os import path
from settings import TILE_SIZE
from map import Camera
movement_speed = 5
rotation_speed = 4

class Player(Sprite):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y, game.all_sprites)
        self.original_image = self.image
        self.angle = 0
        self.game = game
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.rect = self.image.get_rect()
        
        self.dx = 0
        self.dy = 0
        
    
        
    def move(self):
        forward_pressed = is_key_pressed(pygame.K_UP) or is_key_pressed(pygame.K_w)
        backward_pressed = is_key_pressed(pygame.K_DOWN) or is_key_pressed(pygame.K_s)
        left_pressed = is_key_pressed(pygame.K_LEFT) or is_key_pressed(pygame.K_a)
        right_pressed = is_key_pressed(pygame.K_RIGHT) or is_key_pressed(pygame.K_d)
        dx, dy = 0, 0
        if forward_pressed:
            dy -= movement_speed
        elif backward_pressed:
            dy += movement_speed
        if left_pressed:
            dx -= movement_speed
        elif right_pressed:
            dx += movement_speed

        future_rect = self.rect.copy()
        future_rect.topleft = (round(self.x + dx), round(self.y + dy))

        if not any(future_rect.colliderect(wall.rect) for wall in self.game.walls):
            self.x += dx
            self.y += dy
            self.rect.topleft = (round(self.x), round(self.y))

    

    def take_elevator(self):
        now = pygame.time.get_ticks()
        if now - self.game.elev_timer > 1000:
            elevator = pygame.sprite.spritecollideany(self, self.game.elevators)
            if elevator:
                current_floor = self.game.maps.index(self.game.curr_map)

                if pygame.K_e in keys_down:
                    self.game.elev_timer = now
                    self.game.change_floor(current_floor + 1)
                    keys_down.remove(pygame.K_e)
                    
                elif pygame.K_q in keys_down:
                    self.game.elev_timer = now
                    self.game.change_floor(current_floor - 1)
                    keys_down.remove(pygame.K_q)

    def go_to_class(self):
        now = pygame.time.get_ticks()
        if now - self.game.class_timer > 15000:
            classroom = pygame.sprite.spritecollideany(self, self.game.classroom)
            if classroom:
                if pygame.K_e in keys_down:
                    self.game.class_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 17}))
                    keys_down.remove(pygame.K_e)

    def study(self):
        now = pygame.time.get_ticks()
        if now - self.game.study_timer > 60000:
            study = pygame.sprite.spritecollideany(self, self.game.study)
            if study:
                if pygame.K_e in keys_down:
                    self.game.study_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 7}))
                    keys_down.remove(pygame.K_e)

    def hangwfriends(self):
        now = pygame.time.get_ticks()
        if now - self.game.friends_timer > 60000:
            friends = pygame.sprite.spritecollideany(self, self.game.friends)
            if friends:
                if pygame.K_y in keys_down:
                    self.game.friends_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 10}))
                    keys_down.remove(pygame.K_y)

    def petLili(self):
        now = pygame.time.get_ticks()
        if now - self.game.lili_timer > 3000:
            pet = pygame.sprite.spritecollideany(self, self.game.pet)
            if pet:
                if pygame.K_p in keys_down:
                    self.game.lili_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 15}))
                    keys_down.remove(pygame.K_p)

    def takeExam(self):
        now = pygame.time.get_ticks()
        if now - self.game.test_timer > 10000:
            test = pygame.sprite.spritecollideany(self, self.game.test)
            if test:
                if pygame.K_e in keys_down:
                    self.game.test_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 5}))
                    keys_down.remove(pygame.K_e)

    def watchLaLa(self):
        now = pygame.time.get_ticks()
        if now - self.game.movie_timer > 60000:
            movie = pygame.sprite.spritecollideany(self, self.game.movie)
            if movie:
                if pygame.K_v in keys_down:
                    self.game.movie_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 14}))
                    keys_down.remove(pygame.K_v)

    def balcony(self):
        now = pygame.time.get_ticks()
        if now - self.game.balcony_timer > 10000:
            balcony = pygame.sprite.spritecollideany(self, self.game.balcony)
            if balcony:
                if pygame.K_v in keys_down:
                    self.game.balcony_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 12}))
                    keys_down.remove(pygame.K_v)

    def walk(self):
        now = pygame.time.get_ticks()
        if now - self.game.walk_timer > 10000:
            walk = pygame.sprite.spritecollideany(self, self.game.grass)
            if walk:
                if pygame.K_v in keys_down:
                    self.game.walk_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 16}))
                    keys_down.remove(pygame.K_v)

    def grab_coffee(self):
        now = pygame.time.get_ticks()
        if now - self.game.coffee_timer > 18000:
            cof = pygame.sprite.spritecollideany(self, self.game.coffee)
            if cof:
                if pygame.K_v in keys_down:
                    self.game.coffee_timer = now
                    self.game.inv.slots[0].count += 1
                    keys_down.remove(pygame.K_v)
    
    def drink_coffee(self):
        now = pygame.time.get_ticks()
        if (now - self.game.coffee1_timer > 6000) and (pygame.K_SPACE in keys_down) and (self.game.inv.slots[0].count > 0):
            self.game.coffee_timer = now
            self.game.inv.slots[0].count -= 1
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 9}))
            keys_down.remove(pygame.K_SPACE)

    def sleepy(self):
        now = pygame.time.get_ticks()
        if now - self.game.sleep_timer > 60000:
            sleep = pygame.sprite.spritecollideany(self, self.game.sleep)
            if sleep:
                if pygame.K_v in keys_down:
                    self.game.sleep_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 11}))
                    keys_down.remove(pygame.K_v)
                
    def club(self):
        now = pygame.time.get_ticks()
        if now - self.game.club_timer > 3000:
            club = pygame.sprite.spritecollideany(self, self.game.club)
            if club:
                if pygame.K_e in keys_down:
                    self.game.club_timer = now
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 13}))
                    keys_down.remove(pygame.K_e)

    def get_food(self):
        now = pygame.time.get_ticks()
        if now - self.game.food_timer > 3000:
            food = pygame.sprite.spritecollideany(self, self.game.vending)
            if food:
                if pygame.K_v in keys_down:
                    self.game.food_timer = now
                    self.game.inv.slots[4].count += 1
                    keys_down.remove(pygame.K_v)
    
    def eat(self):
        now = pygame.time.get_ticks()
        if (now - self.game.piz_timer > 3000) and (pygame.K_n in keys_down) and (self.game.inv.slots[4].count > 0):
            self.game.piz_timer = now
            self.game.inv.slots[4].count -= 1
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 19}))
            keys_down.remove(pygame.K_n)  
    
    def drop_out(self):
        now = pygame.time.get_ticks()
        if now - self.game.advisor_timer > 1000:
            advisor = pygame.sprite.spritecollideany(self, self.game.advisor)
            if advisor:
                if pygame.K_c in keys_down:
                    print("drop out")
                    self.game.inv.slots[3].count -= 1
                    pygame.event.post(pygame.event.Event(pygame.USEREVENT, {id: 20}))
                    keys_down.remove(pygame.K_c)

    def update(self):
        self.move()
        self.take_elevator()
        self.go_to_class()
        self.hangwfriends()
        self.petLili()
        self.takeExam()
        self.watchLaLa()
        self.balcony()
        self.study()
        self.walk()
        self.grab_coffee()
        self.drink_coffee()
        self.sleepy()
        self.club()
        self.get_food()
        self.eat()
        self.drop_out()



class Lili(Sprite):
    def __init__(self, image, x, y, game):
        self.groups = (game.all_sprites, game.pet)
        super().__init__(image, x, y, self.groups)
        self.original_image = self.image
        self.angle = 0
        self.game = game
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.rect = self.image.get_rect()
        self.direction_timer = 0
    
    def randomMov(self):
        if self.direction_timer <= 0:
            self.dx, self.dy = random.choice([-1, 0, 0, 0, 0 ,1]), random.choice([-1, 0, 0, 0, 0 ,1])
            self.direction_timer = random.randint(40,80)
        else:
            self.direction_timer -= 1
        
        future_rect = self.rect.copy()
        future_rect.topleft = (round(self.x + self.dx), round(self.y + self.dy))
        if not any(future_rect.colliderect(wall.rect) for wall in self.game.walls):
            self.x += self.dx
            self.y += self.dy
            self.rect.topleft = (round(self.x), round(self.y))
        self.x += round(self.dx * movement_speed * .5)
        self.y += round(self.dy * movement_speed * .5)
        self.roll(self.dx, self.dy)
    
    def roll(self, dx, dy):
        direction = -dx if dx != 0 else dy
        self.angle += rotation_speed * direction
        self.image = pygame.transform.rotate(self.original_image, self.angle)
    

