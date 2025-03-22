import pygame
from character import Character

class Cyborg(Character):

    def __init__(self, player_name, max_hp, base_image):
        super().__init__(player_name, max_hp, base_image)
    
    def combo1(self):
        frame = self.getFrame()

        if frame <= 4:
            self.setRect("graphics/cyborg/blast/cyborg_blast1.png")
        elif frame <= 9: 
            self.setRect("graphics/cyborg/blast/cyborg_blast2.png")
        elif frame <= 14:
            self.setRect("graphics/cyborg/blast/cyborg_blast3.png")
        elif frame <= 19:
            self.setRect("graphics/cyborg/blast/cyborg_blast4.png")
        elif frame <= 24:
            self.setRect("graphics/cyborg/blast/cyborg_blast5.png")
        else:
            self.frame = 0
            self.attacking = False
            self.setRect("graphics/cyborg/cyborg_base.png")
