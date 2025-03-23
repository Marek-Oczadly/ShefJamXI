import pygame
import numpy as np
from typing import *


class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, hp: int, base_image: str, player_number: int):
        pygame.sprite.Sprite.__init__(self) 
        
        self.acc: np.ndarray = np.array([0., 0.])
        self.vel: np.ndarray = np.array([0., 0.])

        self.image: pygame.Surface = pygame.transform.scale_by(pygame.image.load(base_image), 0.25)
        self.rect: pygame.Rect = self.image.get_rect()
        self.player_name: str = player_name
        self.hp: int = hp
        self.attacking: bool = False
        self.frame: int = 0
        self.player_number: int = player_number

        # Combo tracking attributes

        self.f_press_count: int = 0
        self.f_last_press_time = 0
        self.combo_pause_limit = 500
        self.current_attack: str = ""

        self.last_hit_time = 0

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

        if self.player_name == "player1":
            self.setRect("graphics/cyborg/cyborg_left.png")
        elif self.player_name == "player2":
            self.setRect("graphics/cyborg/cyborg_left.png")

    def setRect(self, new_file: str):
        current_pos = self.rect.topleft  # Save the current position
        self.image = pygame.image.load(new_file).convert_alpha()
        if self.player_name == "player1":
            self.image = pygame.transform.scale_by(self.image, 0.25)
        if self.player_name == "player2":
            self.image = pygame.transform.scale_by(self.image, 0.25)
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()  # Get the new rect
        self.rect.topleft = current_pos  # Restore the original position
    
    def isOnFloor(self, physicsEngine) -> bool:
        return physicsEngine.isOnFloor(self)[0]
    
    def update(self, keys, physicsEngine):
        self.update_with_controls(keys, self.player_number, physicsEngine)

    def update_with_controls(self, keys, player, physicsEngine) -> None:
        current_time = pygame.time.get_ticks()

        if not self.attacking:
            if player == 1:  # Player 1 controls
                self.handle_player1_input(keys, current_time, physicsEngine)
            elif player == 2:  # Player 2 controls
                self.handle_player2_input(keys, current_time, physicsEngine)
        else:
            self.execute_current_combo()
    
    def handle_player1_input(self, keys, current_time, physicsEngine) -> None:
        # Movement keys for Player 1
        if keys[pygame.K_a] :  # Move left
            if self.isOnFloor(physicsEngine):
                self.vel[0] = max(-5, self.vel[0] - 1)
            else:
                self.vel[0] = max(-5, self.vel[0] - 0.5)
                
        if keys[pygame.K_d]:  # Move right#
            if self.isOnFloor(physicsEngine):
                self.vel[0] = min(5, self.vel[0] + 1)
            else:
                self.vel[0] = min(5, self.vel[0] + 0.5)

        # Jump and combo keys for Player 1
        if keys[pygame.K_SPACE] and self.isOnFloor(physicsEngine):  # Jump
            self.vel[1] = -15

        if keys[pygame.K_f]:  # Attack/Combo
            self.f_press_count += 1
            self.f_last_press_time = current_time
            pygame.time.delay(150)
        elif self.f_press_count > 0 and current_time - self.f_last_press_time > self.combo_pause_limit:
            self.trigger_combo()


    def handle_player2_input(self, keys, current_time, physicsEngine):
        # Movement keys for Player 2
        if keys[pygame.K_LEFT] :  # Move left
            if self.isOnFloor(physicsEngine):
                self.vel[0] = max(-5, self.vel[0] - 1)
            else:
                self.vel[0] = max(-5, self.vel[0] - 0.5)
                
        if keys[pygame.K_RIGHT]:  # Move right
            if self.isOnFloor(physicsEngine):
                self.vel[0] = min(5, self.vel[0] + 1)
            else:
                self.vel[0] = min(5, self.vel[0] + 0.5)

        # Jump and combo keys for Player 2
        if keys[pygame.K_UP] and self.isOnFloor(physicsEngine):  # Jump
            self.vel[1] = -15
            print("Player 2 jumped")


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


class StaticObject(pygame.sprite.Sprite):
    
    def __init__(self, path: Union[BinaryIO, str], coords: Tuple[int, int]):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = coords[0], coords[1]
        
    def getRect(self) -> pygame.Rect:
        return self.rect
    
    def getImage(self) -> pygame.Surface:
        return self.image


class Bar:
    def __init__(self, fn: Callable[[], float], coords: Tuple[int, int], 
                 max_dim: Tuple[int, int], colours: Tuple[str] = ("Grey", "Green")):
        pygame.sprite.Sprite.__init__(self)
        self.size_fn = fn
        self.colours = colours
        self.coords = coords
        self.maxdim = max_dim
    
    def display(self, screen: pygame.Surface) -> None:
        length: float = self.size_fn()
        pygame.draw.rect(screen, self.colours[0], (*self.coords, *self.maxdim))
        pygame.draw.rect(screen, self.colours[1], (*self.coords, length,self.maxdim[1]))
        

class GameOver(pygame.sprite.Sprite):
    def __init__(self, coords: Tuple[int, int], path: Union[BinaryIO, str]):
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
    
    def display(self, screen):
        screen.blit(self.image, self.rect)
        