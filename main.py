import pygame
from sys import exit
from cyborg import Cyborg
from two_face import TwoFace
from character import StaticObject, Bar
import physics

class Main:
    def __init__(self):
        # Initialize Player 1 (Cyborg) and Player 2 (Two-Face)
        # self.player1 = Cyborg("player1", 100, "graphics/cyborg/cyborg_base.png", 1)
        # self.player2 = Cyborg("player2", 100, "graphics/cyborg/cyborg_base.png", 2)
        
        self.physicsEngine: physics.PhysicsEngine = physics.PhysicsEngine()
        
        # Set initial positions
        # self.player1.rect.bottomleft = (10, 300)  # Left side of the screen
        # self.player2.rect.bottomleft = (550, 300)  # Right side of the screen

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Two-Player Game")
        clock = pygame.time.Clock()

        # Setting up engine
        i = self.physicsEngine.addCharacter(Cyborg("player1", 100, "graphics/cyborg/cyborg_base.png", 1), (10, 300))
        j = self.physicsEngine.addCharacter(Cyborg("player2", 100, "graphics/cyborg/cyborg_base.png", 2), (550, 300))
        self.physicsEngine.addStatic(StaticObject("graphics/ground.png", (0, 300)))
        self.physicsEngine.setBackground(StaticObject("graphics/Sky.png", (0, 0)))
        self.physicsEngine.addAmbient(Bar(lambda: self.physicsEngine.characters[i].getHealth() * 2, (30, 10), (200, 30)))
        self.physicsEngine.addAmbient(Bar(lambda: self.physicsEngine.characters[j].getHealth() * 2, (570, 10), (200, 30)))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            # if self.player1.attacking and self.player1.check_collision(self.player2):
            #     self.player1.apply_damage(self.player2, 10)  # Player 2 takes 10 damage
            #     print(self.player2.hp)

            # if self.player2.attacking and self.player2.check_collision(self.player1):
            #     self.player1.apply_damage(self.player1, 10)
            #     self.player1.hp -= 10  # Reduce Player 1's health by 10

            # self.player1.draw_attack_hitbox(screen)
            # self.player2.draw_attack_hitbox(screen)

            # pygame.draw.rect(screen, "Green", self.player1.rect, 2)
            # pygame.draw.rect(screen, "Green", self.player2.rect, 2)
            
            self.physicsEngine.update(keys)
            pygame.display.update()
            self.physicsEngine.blitAll(screen)
            clock.tick(60)


if __name__ == "__main__":
    app = Main()
    app.run()