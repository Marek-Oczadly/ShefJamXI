import pygame
from typing import *
from sys import exit
import numpy as np

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My game", False, "Black")

snail_surface = pygame.image.load("graphics/Snail/snail1.png").convert_alpha()
snail_x_pos = 600

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(ground_surface,(0,300))
    screen.blit(sky_surface, (0,0))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))
    player_rect.left += 1 
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)