import pygame
import numpy as np
from typing import *


class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
        
        self.acc = np.array([0., 0.])
        self.vel = np.array([0., 0.])

        self.image = pygame.transform.scale_by(pygame.image.load(base_image), 0.25)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp

    # make it move, given array of keys
    def move(self, direction):
        self.rect = self.rect.move(direction, 0)
        
    def end_jump(self):
        print("ended jump")
        self.jump_frame = None

    # first combo, should be defined in subclass
    def combo1(self, keys):
        pass

    def setRect(self, new_file: str):
        self.image = pygame.image.load(new_file).convert_alpha()
        self.rect = self.image.get_rect()
        
    def isOnFloor(self) -> bool:
        return self.rect.bottom >= 300

    def update(self, keys):
        if self.rect.bottom > 300:
            self.rect.move(0, self.rect.bottom - 299)
            
        if keys[pygame.K_a]:
            self.vel[0] = -5
        if keys[pygame.K_d]:
            self.vel[0] = 5
        if keys[pygame.K_SPACE] and self.isOnFloor():
            self.vel[1] = -8
    
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect
    