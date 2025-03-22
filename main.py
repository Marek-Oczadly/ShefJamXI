import pygame
from sys import exit
from character import Character
from cyborg import Cyborg
from two_face import TwoFace

class Main:
    def __init__(self):
        # Initialize Player 1 (Cyborg) and Player 2 (Two-Face)
        self.player1 = Cyborg("Cyborg", 100, "graphics/cyborg/cyborg_base.png")
        self.player2 = TwoFace("Two-Face", 100, "graphics/two_face/two_face_base.png")

        # Set initial positions
        self.player1.rect.bottomleft = (50, 300)  # Left side of the screen
        self.player2.rect.bottomleft = (500, 300)  # Right side of the screen

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Two-Player Game")
        clock = pygame.time.Clock()

        # Background surfaces
        sky_surface = pygame.image.load("graphics/sky.png").convert()
        ground_surface = pygame.image.load("graphics/ground.png").convert()

        while True:
            screen.blit(ground_surface, (0, 300))
            screen.blit(sky_surface, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            # Update both players
            self.player1.update_with_controls(keys, player=1)
            self.player2.update_with_controls(keys, player=2)

            # Render both players
            screen.blit(self.player1.getImg(), self.player1.getRect())
            screen.blit(self.player2.getImg(), self.player2.getRect())

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    app = Main()
    app.run()