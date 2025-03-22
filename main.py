import pygame
from sys import exit
from cyborg import Cyborg
from character import StaticObject
import physics

class Main:
    def __init__(self):
        self.physicsEngine = physics.PhysicsEngine(gravity=-8)
        self.physicsEngine.addCharacter(Cyborg("Charlie", 100, "graphics/cyborg/cyborg_base.png"))
        self.physicsEngine.addStatic(StaticObject("graphics/ground.png", (0, 300)))

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400)) 
        pygame.display.set_caption("Game")
        clock = pygame.time.Clock()


        sky_surface = pygame.image.load("graphics/Sky.png").convert()
        self.physicsEngine.init()
        self.screen.blit(sky_surface, (0,0))
        
        while True:
            self.screen.blit(sky_surface, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.physicsEngine.update(pygame.key.get_pressed())
            self.physicsEngine.blitAll(self.screen)

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    app = Main()
    app.run()