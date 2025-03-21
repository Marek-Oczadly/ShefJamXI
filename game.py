import pygame 

pygame.init() 

color = (255,255,255) 
rect_color = (255,0,0) 

# CREATING CANVAS 
canvas = pygame.display.set_mode((500,500)) 

# TITLE OF CANVAS 
pygame.display.set_caption("Show Image") 

<<<<<<< HEAD
image = pygame.image.load("MAREK.jpg") 
=======
>>>>>>> 8c297ba4b1cfab152121469f5b61ea8c9eba1fc6
exit = False

while not exit: 
	canvas.fill(color) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			exit = True

	pygame.draw.rect(canvas, rect_color, 
					pygame.Rect(30,30,60,60)) 
	pygame.display.update() 

