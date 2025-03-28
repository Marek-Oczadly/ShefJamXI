import pygame
from character import Character

class Cyborg(Character):

    def __init__(self, player_name, max_hp, base_image, player_number):
        super().__init__(player_name, max_hp, base_image, player_number)
        self.combos = {
            "combo1": [
                (4, "graphics/cyborg/slash/cyborg_slash1.png"),
                (9, "graphics/cyborg/slash/cyborg_slash2.png"),
                (14, "graphics/cyborg/slash/cyborg_slash3.png"),
                (19, "graphics/cyborg/slash/cyborg_slash4.png"),
                (24, "graphics/cyborg/slash/cyborg_slash5.png")
            ],
            "combo2": [
                (4, "graphics/cyborg/chest_blast/cyborg_chest1.png"),
                (9, "graphics/cyborg/chest_blast/cyborg_chest2.png"),
                (14, "graphics/cyborg/chest_blast/cyborg_chest3.png"),
                (19, "graphics/cyborg/chest_blast/cyborg_chest4.png"),
                (24, "graphics/cyborg/chest_blast/cyborg_chest5.png")
            ],
            "combo3": [
                (4, "graphics/cyborg/blast/cyborg_blast1.png"),
                (9, "graphics/cyborg/blast/cyborg_blast2.png"),
                (14, "graphics/cyborg/blast/cyborg_blast3.png"),
                (19, "graphics/cyborg/blast/cyborg_blast4.png"),
                (24, "graphics/cyborg/blast/cyborg_blast5.png")
            ],
            "combo4": [
                (4, "graphics/cyborg/eye_shot/cyborg_shot1.png"),
                (9, "graphics/cyborg/eye_shot/cyborg_shot2.png"),
                (14, "graphics/cyborg/eye_shot/cyborg_shot3.png"),
                (19, "graphics/cyborg/eye_shot/cyborg_shot4.png"),
                (24, "graphics/cyborg/eye_shot/cyborg_shot5.png")
            ]
        }

    
