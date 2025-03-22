import pygame
from character import Character

class Cyborg(Character):

    def __init__(self, player_name, max_hp, base_image):
        super().__init__(player_name, max_hp, base_image)
    
    def combo1(self):
        frame_data = [
            (4, "graphics/cyborg/blast/cyborg_blast1.png"),
            (9, "graphics/cyborg/blast/cyborg_blast2.png"),
            (14, "graphics/cyborg/blast/cyborg_blast3.png"),
            (19, "graphics/cyborg/blast/cyborg_blast4.png"),
            (24, "graphics/cyborg/blast/cyborg_blast5.png")
        ]
        self.setComboFrame(self.frame, frame_data)
