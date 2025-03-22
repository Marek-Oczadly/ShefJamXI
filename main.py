import pygame
from sys import exit

class Main:
    def __init__(self):
        self.player1 = Cyborg()
        self.player2 = Playboi()
        pass

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Game")
        clock = pygame.time.Clock()

        sky_surface = pygame.image.load("graphics/Sky.png").convert()
        ground_surface = pygame.image.load("graphics/ground.png").convert()

        screen.blit(ground_surface,(0,300))
        screen.blit(sky_surface, (0,0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            keys = pygame.key.get_pressed()

            result_p1 = self.player1.update(keys)
            result_p2 = self.player2.update(keys)

            pygame.display.update()
            clock.tick(60)


if __name__ == "__main__":
    app = Main()
    app.run()