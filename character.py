import pygame
from typing import *


def jump(initial_v: float, frame: int, gravity: float = -7, frame_rate: int = 60, pixels_per_meter: int = 200) -> float :
    gravity_new_units = (gravity * pixels_per_meter) / (frame_rate * frame_rate)
    v = initial_v + gravity_new_units * frame
    return v

def move():
    pass


class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, hp: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.hp = hp
        self.jump_frame = None
        self.attacking = False
        self.frame = 0

        # Combo tracking attributes

        self.f_press_count = 0
        self.f_last_press_time = 0
        self.combo_pause_limit = 500
        self.current_attack = ""

        self.last_hit_time = 0

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
    
    def execute_combo(self, frame_data):
        self.setComboFrame(self.frame, frame_data)
    
    def resetAnimation(self):
        self.frame = 0

        self.attacking = False

        self.setRect("graphics/cyborg/cyborg_base.png")

    def setRect(self, new_file: str):
        current_pos = self.rect.topleft  # Save the current position
        self.image = pygame.image.load(new_file).convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()  # Get the new rect
        self.rect.topleft = current_pos  # Restore the original position
        
    def isOnFloor(self) -> bool:
        return self.rect.bottom >= 300

    def update_with_controls(self, keys, player):
        current_time = pygame.time.get_ticks()

        if not self.attacking:
            if player == 1:  # Player 1 controls
                self.handle_player1_input(keys, current_time)
            elif player == 2:  # Player 2 controls
                self.handle_player2_input(keys, current_time)
        else:
            self.execute_current_combo()
    
    def handle_player1_input(self, keys, current_time):
        # Movement keys for Player 1
        if keys[pygame.K_a]:  # Move left
            self.move(-5)
        if keys[pygame.K_d]:  # Move right
            self.move(5)

        # Jump and combo keys for Player 1
        if keys[pygame.K_SPACE] and self.jump_frame is None:  # Jump
            self.begin_jump()
        if self.jump_frame is not None:
            self.jump()

        if keys[pygame.K_f]:  # Attack/Combo
            self.f_press_count += 1
            self.f_last_press_time = current_time
            pygame.time.delay(150)
        elif self.f_press_count > 0 and current_time - self.f_last_press_time > self.combo_pause_limit:
            self.trigger_combo()


    def handle_player2_input(self, keys, current_time):
        # Movement keys for Player 2
        if keys[pygame.K_LEFT]:  # Move left
            self.move(-5)
        if keys[pygame.K_RIGHT]:  # Move right
            self.move(5)

        # Jump and combo keys for Player 2
        if keys[pygame.K_j] and self.jump_frame is None:  # Jump
            self.begin_jump()
        if self.jump_frame is not None:
            self.jump()

        if keys[pygame.K_p]:  # Attack/Combo
            self.f_press_count += 1
            self.f_last_press_time = current_time
            pygame.time.delay(150)
        elif self.f_press_count > 0 and current_time - self.f_last_press_time > self.combo_pause_limit:
            self.trigger_combo()
    
    def trigger_combo(self):
        if self.f_press_count >= 4:
            self.current_attack = "combo4"
        elif self.f_press_count >= 3:
            self.current_attack = "combo3"
        elif self.f_press_count >= 2:
            self.current_attack = "combo2"
        elif self.f_press_count >= 1:
            self.current_attack = "combo1"
        
        self.attacking = True
        self.f_press_count = 0  # Reset press count after triggering a combo
    
    def execute_current_combo(self):
        if self.current_attack:
            self.execute_combo(self.combos[self.current_attack])  # Execute the combo
        self.frame += 0.5

    def get_attack_rect(self):

        if self.current_attack:  # If the player is attacking
            # Extend the hitbox to the right if facing right
            if self.player_name == "player1":  # Example: Assuming facing right by default
                return pygame.Rect(self.rect.left+self.rect.width/2, self.rect.y + int(self.rect.height * (1 - 0.8) / 2),
                                self.rect.width / 5, int(self.rect.height * 0.8))
            else:  # Extend hitbox to the left if facing left
                return pygame.Rect(self.rect.left, self.rect.y + int(self.rect.height * (1 - 0.8) / 2),
                                self.rect.width / 5, int(self.rect.height * 0.8))
        return None
    
    def check_collision(self, opponent):
        attack_rect = self.get_attack_rect()
        if attack_rect and attack_rect.colliderect(opponent.rect):  # Check for overlap
            return True
        return False
    
    def apply_damage(self, opponent, damage_amount, current_time):
        if current_time - self.last_hit_time > 1500:  # 3s cooldown
            opponent.hp -= damage_amount
            self.last_hit_time = current_time

    def draw_attack_hitbox(self, screen):
        attack_rect = self.get_attack_rect()
        if attack_rect:
            pygame.draw.rect(screen, (255, 0, 0), attack_rect, 2)  # Draw a red outline for the hitbox
    
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect
    
    def getFrame(self):
        return self.frame
    
    def getHealth(self):
        return self.hp
    
    def setFrame(self, newF):
        self.frame = newF
