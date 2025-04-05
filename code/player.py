import pygame
import random
from sprite import Sprite
from input import is_key_pressed, keys_down
from os import path
from settings import TILE_SIZE
from map import Camera
movement_speed = 5
rotation_speed = 3

class Player(Sprite):
    def __init__(self, image, x, y, game):
        super().__init__(image, x, y, game.all_sprites)
        self.original_image = self.image
        self.angle = 0
        self.game = game
        self.x = x*TILE_SIZE
        self.y = y*TILE_SIZE
        self.rect = self.image.get_rect()
        self.direction_timer = 0
        self.dx = 0
        self.dy = 0
        
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

    def roll(self, dx, dy):
        direction = -dx if dx != 0 else dy
        self.angle += rotation_speed * direction
        self.image = pygame.transform.rotate(self.original_image, self.angle)

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
                    

    def update(self):
        self.move()
        self.take_elevator()




