import pygame
from typing import *

def jump(initial_v: float, frame: int, gravity: float = -5.5, frame_rate: int = 60, pixels_per_meter: int = 30) -> float :
    gravity_new_units = (gravity * pixels_per_meter) / (frame_rate * frame_rate)
    return initial_v + gravity_new_units * frame


class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp

    # make it move, given array of keys
    def move(self, direction):
        self.rect.move(direction, 0)

    # make it jump, given array of keys
    def jump(self, keys):
        pass

    # first combo, should be defined in subclass
    def combo1(self, keys):
        pass

    def setRect(self, new_file: str):
        self.image = pygame.image.load(new_file).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, screen, keys):

        if keys[pygame.K_s]:
            self.move(5)
        self.load(screen)

    def load(self, screen):
        screen.blit(self.image, self.rect)