#learning pygame
import pygame

pygame.init() #initialise the pygame

#create the screen
screen = pygame.display.set_mode((800, 600)) #height, width of window to create

# -- an event is anything that is happening inside your game window i.e. pressing a key

running = True
while running: #creates infinite loop so game window stays on screen and program doesnt end
    for event in pygame.event.get(): #checking if close button has been checked
         if event.type == pygame.QUIT:
              running = False #close program (program ends after while loop)
