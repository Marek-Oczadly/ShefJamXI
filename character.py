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

        # Combo tracking attributes

        self.f_press_count = 0
        self.combo_timer = 0
        self.combo_time_limit = 1000

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
            if keys[pygame.K_a]:  # Move left
                self.move(-5)
            if keys[pygame.K_d]:  # Move right
                self.move(5)
            if keys[pygame.K_SPACE] and self.jump_frame is None:  # Begin jump
                self.begin_jump()

            # Continue jump if in progress
            if self.jump_frame is not None:
                self.jump()

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
