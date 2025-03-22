import pygame
from typing import *

def jump(initial_v: float, frame: int, gravity: float = -5.5, frame_rate: int = 60, pixels_per_meter: int = 30) -> float :
    gravity_new_units = (gravity * pixels_per_meter) / (frame_rate * frame_rate)
    return initial_v + gravity_new_units * frame



class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, height: int, width: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp

    # make it move, given array of keys
    def move(keys):
        pass

    # make it jump, given array of keys
    def jump(keys):
        pass

    # first combo, should be defined in subclass
    def combo1(keys):
        pass

if __name__ == "__main__":
    