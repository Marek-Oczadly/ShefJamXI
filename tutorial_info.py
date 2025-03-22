#learning pygame
import pygame
import random
import math

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

#background image
background = pygame.image.load("graphics/space-background.png")

#ADDING IMAGES INTO GAME WINDOW
#PLAYER
playerImg = pygame.image.load("graphics/space-player.png")
playerX = 670 #x-coord of image
playerY = 380 #y-coord of image
playerX_change = 0
playerY_change = 0
player_score = 0

def player(x,y):
    screen.blit(playerImg, (x, y)) #draws loaded image on screen

#ENEMY
enemyImg = pygame.image.load("graphics/space-enemy.png")
enemyX = random.randint(0, 736) #enemy spawns at random points in game window
enemyY = random.randint(0, 536) 
enemyX_change = 4
enemyY_change = 4

def enemy(x,y):
    screen.blit(enemyImg, (x,y))

#SHURIKEN
# "ready" - shuriken cannot be seen on screen
# "fire" - shuriken is currently moving
shurikenImg = pygame.image.load("graphics/shuriken.png")
shurikenX = 0
shurikenY = 0
shurikenX_change = 10
shuriken_state = "ready"; 

def fire_shuriken(x,y):
    global shuriken_state #global lets variable be accessed within method
    shuriken_state = "fire"
    screen.blit(shurikenImg, (x - 10, y + 30))

#COLLISION DETECTION
def isCollision(eX, eY, sX, sY):
    #equation for distance between two points
    distance = math.sqrt((math.pow(eX - sX,2)) + (math.pow(eY - sY,2)))
    if distance < 25:
        return True
    else:
        return False

#CREATING THE GAME LOOP - ensures game doesnt close until close button is pressed, where the game is actually run from
running = True
while running: 
    #background colour and image
    screen.fill((166, 0, 255))
    screen.blit(background, (0, 0)) #makes game run slower as image is loaded upon every iteration in the while loop

    for event in pygame.event.get(): #checking if close button has been checked
        if event.type == pygame.QUIT:
            running = False #close program (program ends after while loop)

        #KEYBOARD INPUT MECHANICS AND KEY PRESS EVENT   
        #if keystroke pressed, checked whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            elif event.key == pygame.K_RIGHT:
                playerX_change = 5
            elif event.key == pygame.K_UP:
                playerY_change = -5
            elif event.key == pygame.K_DOWN:
                playerY_change = 5
            elif event.key == pygame.K_SPACE:
                if shuriken_state == "ready":
                    #get current coordinate of player, then fire
                    shurikenX = playerX
                    shurikenY = playerY
                    fire_shuriken(shurikenX, shurikenY)
        if event.type == pygame.KEYUP: #keypress released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerX_change = 0
                playerY_change = 0
        
    #ADDING BOUNDARIES TO GAME WINDOW (while controlling player and enemy movement)
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

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4 #enemy moves away from boundary
    elif enemyX >= 736:
        enemyX_change = -4
    
    enemyY += enemyY_change
    if enemyY <= 0:
        enemyY_change = 4
    elif enemyY >= 536:
        enemyY_change = -4

    player(playerX, playerY) 

    #SHURIKEN MOVEMENT
    #ensures shuriken cannot be fired until last one exits screen
    if shurikenX <= 0:
        shurikenX = playerX
        shuriken_state = "ready"
    if shuriken_state == "fire":
        fire_shuriken(shurikenX, shurikenY)
        shurikenX -= shurikenX_change 

    #COLLISION
    collision = isCollision(enemyX, enemyY, shurikenX, shurikenY)
    if collision:
        #reset shuriken to its starting point (the player)
        #screen.blit(collisionImg, (shurikenX, shurikenY))
        shurikenX = playerX
        shurikenY = playerY
        shuriken_state = "ready" #because shuriken isnt being shown anymore
        player_score = player_score + 1
        print(player_score)
        collision = False
        enemyX = random.randint(0, 736)
        enemyY = random.randint(0, 536) 

    enemy(enemyX, enemyY)
    pygame.display.update() #ensures game window is updated everytime something is added

        


