import pygame
from typing import *


def jump(initial_v: float, frame: int, gravity: float = -7, frame_rate: int = 60, pixels_per_meter: int = 200) -> float :
    gravity_new_units = (gravity * pixels_per_meter) / (frame_rate * frame_rate)
    v = initial_v + gravity_new_units * frame
    return v

def move():
    pass


class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp
        self.jump_frame = None
        self.attacking = False
        self.frame = 0

    # make it move, given array of keys
    def move(self, direction):
        self.rect = self.rect.move(direction, 0)

    def begin_jump(self):
        self.jump_frame = 0
        self.jump()
    
    # make it jump, given array of keys
    def jump(self):
        self.rect = self.rect.move(0, -jump(10, self.jump_frame))
        self.jump_frame += 1
        if self.isOnFloor():
            self.end_jump()
        
    def end_jump(self):
        print("ended jump")
        self.jump_frame = None

    # first combo, should be defined in subclass
    def combo1(self):
        pass

    def setRect(self, new_file: str):
        self.image = pygame.image.load(new_file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        
    def isOnFloor(self) -> bool:
        return self.rect.bottom >= 300

    def update(self, keys):
        if not self.attacking:
            if keys[pygame.K_a]:
                self.move(-5)
            if keys[pygame.K_d]:
                self.move(5)
            if keys[pygame.K_SPACE] and self.jump_frame is None:
                self.begin_jump()
            if keys[pygame.K_f]:
                self.attacking = True
            
            if self.jump_frame is not None:
                self.jump()
        else:
            self.combo1()
            self.frame += 0.5
    
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect
    
    def getFrame(self):
        return self.frame
    
    def setFrame(self, newF):
        self.frame = newF
