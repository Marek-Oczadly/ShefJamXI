import pygame
from typing import *;


def getDirection() -> Tuple[int, int]:
    keys_pressed = pygame.key.get_pressed()
    direction_x: int = 0
    direction_y: int = 0
    if keys_pressed[pygame.K_w]:
        direction_x += 1
    if keys_pressed[pygame.K_s]:
        direction_x -= 1
    if keys_pressed[pygame.K_d]:
        direction_y += 1
    if keys_pressed[pygame.K_a]:
        direction_y -= 1
    return direction_x, direction_y