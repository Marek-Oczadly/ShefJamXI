#learning pygame
import pygame

# --ADDITIONAL NOTES:
# -- an event is anything that is happening inside your game window i.e. pressing a key

pygame.init() #initialise the pygame

#CREATING THE GAME WINDOW
#create the screen
screen = pygame.display.set_mode((800, 600)) #width and height of window to create

#CHANGING TITLE, LOGO, BACKGROUND
#title and icon
pygame.display.set_caption("Spacey Vaders")
icon = pygame.image.load("graphics/galaxy.png")
pygame.display.set_icon(icon)

#ADDING IMAGES INTO GAME WINDOW
#Player
playerImg = pygame.image.load("graphics/space-player.png")
playerX = 670 #x-coord of image
playerY = 380 #y-coord of image
playerX_change = 0
playerY_change = 0


def player(x,y):
    screen.blit(playerImg, (x, y)) #draws loaded image on screen






#CREATING THE GAME LOOP - ensures game doesnt close until close button is pressed
running = True
while running: 
    #background colour
    screen.fill((166, 0, 255))

    for event in pygame.event.get(): #checking if close button has been checked
        if event.type == pygame.QUIT:
            running = False #close program (program ends after while loop)

        #KEYBOARD INPUT MECHANICS AND KEY PRESS EVENT   
        #if keystroke pressed, checked whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            elif event.key == pygame.K_UP:
                playerY_change = -0.1
            elif event.key == pygame.K_DOWN:
                playerY_change = 0.1
        if event.type == pygame.KEYUP: #keypress released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
        

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536
    player(playerX, playerY) 
    pygame.display.update() #ensures game window is updated everytime something is added

        


