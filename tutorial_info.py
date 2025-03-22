#learning pygame
import pygame
import random
import math
from pygame import mixer #class that handles sounds (loading, repeating etc)

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

#background image and sound
background = pygame.image.load("graphics/space-background.png")
mixer.music.load("audio/game-background.wav") #use .music for sounds that will play continuously/for a while
mixer.music.play(-1) #loops the sound

#ADDING IMAGES INTO GAME WINDOW
#PLAYER
playerImg = pygame.image.load("graphics/space-player.png")
playerX = 670 #x-coord of image
playerY = 380 #y-coord of image
playerX_change = 0
playerY_change = 0

#SCORE
player_score = 0
font = pygame.font.Font('font/Pixeltype.ttf', 48)
textX = 10 #coordinates of the text
textY = 10

#GAME OVER
game_over_font = pygame.font.Font('font/Pixeltype.ttf', 96)


def show_score(x, y):
    score = font.render("Score: " + str(player_score), True, (255, 100, 221)) #true = show score, put colour
    screen.blit(score, (x, y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (254, 284))

def player(x,y):
    screen.blit(playerImg, (x, y)) #draws loaded image on screen

#ENEMY - MULTIPLE ENEMIES
enemyImg = []
enemyX = []
enemyY = [] 
enemyX_change = [] 
enemyY_change = []
num_of_enemies = 2

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load("graphics/space-enemy.png"))
    enemyX.append(random.randint(0, 736)) #enemy spawns at random points in game window
    enemyY.append(random.randint(0, 536)) 
    enemyX_change.append(2)
    enemyY_change.append(2)

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y))

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
                    #shuriken throw sound
                    shuriken_sound = mixer.Sound("audio/shuriken-throw.wav")
                    shuriken_sound.play()
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

    #ENEMY MOVEMENT
    for i in range(num_of_enemies):

        #GAME OVER
        if abs(playerX - enemyX[i]) < 4 and abs(playerY - enemyY[i] < 4):
            for j in range(num_of_enemies):
                playerY = 2000
                enemyY[j] = 2000 #get all enemies off the screen
            game_over_text()
            pygame.quit()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2 #enemy moves away from boundary
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
        
        enemyY[i] += enemyY_change[i]
        if enemyY[i] <= 0:
            enemyY_change[i] = 2
        elif enemyY[i] >= 536:
            enemyY_change[i] = -2

        #COLLISION
        collision = isCollision(enemyX[i], enemyY[i], shurikenX, shurikenY)
        if collision:
            #collision sound
            collision_sound = mixer.Sound("audio/explosion.wav")
            collision_sound.play()
            #screen.blit(collisionImg, (shurikenX, shurikenY))
            #reset shuriken to its starting point (the player)
            shurikenX = playerX
            shurikenY = playerY
            shuriken_state = "ready" #because shuriken isnt being shown anymore
            player_score = player_score + 1
            collision = False
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 536) 

        enemy(enemyX[i], enemyY[i], i)

    player(playerX, playerY) 

    #SHURIKEN MOVEMENT
    #ensures shuriken cannot be fired until last one exits screen
    if shurikenX <= 0:
        shurikenX = playerX
        shuriken_state = "ready"
    if shuriken_state == "fire":
        fire_shuriken(shurikenX, shurikenY)
        shurikenX -= shurikenX_change 

    show_score(textX, textY)
    pygame.display.update() #ensures game window is updated everytime something is added 
