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
        self.attacking = False
        self.frame = 0

        # Combo tracking attributes

        self.f_press_count = 0
        self.combo_timer = 0
        self.combo_time_limit = 1000

        # self.combo_thresholds = {3: self.combo1, 5: self.combo2}

    # first combo, should be defined in subclass
    def combo1(self):
        pass

    def setComboFrame(self, frame, frame_data):
        for limit, image in frame_data:
            if frame <= limit:
                self.setRect(image)
                return 
        self.resetAnimation()
    
    def resetAnimation(self):
        self.frame = 0

        self.attacking = False

        self.setRect("graphics/cyborg/cyborg_base.png")

    def setRect(self, new_file: str):
        self.image = pygame.image.load(new_file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        
    def isOnFloor(self) -> bool:
        return self.rect.bottom >= 300

    def update(self, keys):
        current_time = pygame.time.get_ticks()

        # Check if combo timer should reset
        if self.combo_timer > 0 and current_time - self.combo_timer > self.combo_time_limit:
            self.f_press_count = 0
            self.combo_timer = 0

        if not self.attacking:
            # Handle key presses for movement and jumping
            if keys[pygame.K_a]:
                self.vel[0] = -5
            if keys[pygame.K_d]:
                self.vel[0] = 5
            if keys[pygame.K_SPACE] and self.isOnFloor():
                self.vel[1] = -8

            # Track 'f' presses for combo
            if keys[pygame.K_f]:
                if self.f_press_count == 0:  # First press starts the timer
                    self.combo_timer = current_time
                self.f_press_count += 1
                pygame.time.delay(150)  # Prevent rapid key polling for a single press

            # Trigger combo if the threshold is met
            if self.f_press_count >= 3:
                self.attacking = True
                self.combo_timer = 0
                self.f_press_count = 0

        else:
            # Perform combo if in attacking state
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
