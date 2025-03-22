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
        self.f_last_press_time = 0
        self.combo_pause_limit = 500
        self.current_attack = ""

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

        if not self.attacking:
            # Handle key presses for movement and jumping
            if keys[pygame.K_a]:
                self.move(-5)
            if keys[pygame.K_d]:
                self.move(5)
            if keys[pygame.K_SPACE] and self.jump_frame is None:
                self.begin_jump()
            if self.jump_frame is not None:
                self.jump()

            # Detect 'f' presses
            if keys[pygame.K_f]:
                # Increment press count and update the last press timestamp
                self.f_press_count += 1
                self.f_last_press_time = current_time
                pygame.time.delay(150)  # Prevent rapid polling for a single press

            # Detect a pause after the last 'f' press
            elif self.f_press_count > 0 and current_time - self.f_last_press_time > self.combo_pause_limit:
                # Decide which combo to activate based on the press count
                if self.f_press_count >= 4:
                    self.combo5()  # Trigger the 4-click combo
                    self.current_attack = "combo5"
                elif self.f_press_count >= 3:
                    self.combo4()  # Trigger the 3-click combo
                    self.current_attack = "combo4"
                elif self.f_press_count >= 2:
                    self.combo2()
                    self.current_attack = "combo2"
                elif self.f_press_count >= 1:
                    self.combo1()
                    self.current_attack = "combo1"
                
                self.attacking = True
                
                self.f_press_count = 0  # Reset press count after combo

        else:
            # Continue the current combo
            match self.current_attack:
                case "combo1":
                    self.combo1()
                case "combo2":
                    self.combo2()
                case "combo3":
                    pass
                case "combo4":
                    self.combo4()
                case "combo5":
                    self.combo5()
            self.frame += 0.5
        
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect
    
    def getFrame(self):
        return self.frame
    
    def setFrame(self, newF):
        self.frame = newF
