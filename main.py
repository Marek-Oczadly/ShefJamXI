import pygame
from sys import exit
from cyborg import Cyborg
from two_face import TwoFace
from character import StaticObject, Bar
import physics

class Main:
    def __init__(self):
        # Initialize Player 1 (Cyborg) and Player 2 (Two-Face)
        self.physicsEngine = physics.PhysicsEngine()

        
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Two-Player Game")
        clock = pygame.time.Clock()

        # Setting up engine
        player_1 = self.physicsEngine.addCharacter(Cyborg("player1", 100, "graphics/cyborg/cyborg_base.png", 1), (10, 300))
        player_2 = self.physicsEngine.addCharacter(TwoFace("player2", 100, "graphics/two_face/two_face_base.png", 2), (550, 345))
        self.physicsEngine.addStatic(StaticObject("graphics/ground.png", (0, 300)))
        self.physicsEngine.setBackground(StaticObject("graphics/Sky.png", (0, 0)))
        self.physicsEngine.addAmbient(Bar(lambda: player_1.getHealth() * 2, (30, 10), (200, 30)))
        self.physicsEngine.addAmbient(Bar(lambda: player_2.getHealth() * 2, (570, 10), (200, 30)))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()
            current_time = pygame.time.get_ticks()

            if player_1.attacking and player_1.check_collision(player_2):
                player_1.apply_damage(player_2, 10, current_time)  # Player 2 takes 10 damage

            if player_2.attacking and player_2.check_collision(player_1):
                player_1.apply_damage(player_1, 10, current_time)

        
            
            self.physicsEngine.update(keys)
            pygame.display.update()
            self.physicsEngine.blitAll(screen)
            pygame.draw.rect(screen, "Green", player_1.rect, 2)
            pygame.draw.rect(screen, "Green", player_2.rect, 2)
            player_1.draw_attack_hitbox(screen)
            player_2.draw_attack_hitbox(screen)
            
            clock.tick(60)


if __name__ == "__main__":
    app = Main()
    app.run()