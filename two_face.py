import pygame
from character import Character

class TwoFace(Character):
    def __init__(self, player_name, max_hp, base_image):
        super().__init__(player_name, max_hp, base_image)

    def __init__(self, player_name, max_hp, base_image):
        super().__init__(player_name, max_hp, base_image)
        self.combos = {
            "combo1": [
                (4, "graphics/two_face/blast/two_face_blast_1.png"),
                (9, "graphics/two_face/blast/two_face_blast_2.png"),
                (14, "graphics/two_face/blast/two_face_blast_3.png"),
                (19, "graphics/two_face/blast/two_face_blast_4.png"),
                (24, "graphics/two_face/blast/two_face_blast_5.png")
            ],
            "combo2": [
                (4, "graphics/two_face/missile/two_face_missile_1.png"),
                (9, "graphics/two_face/missile/two_face_missile_2.png"),
                (14, "graphics/two_face/missile/two_face_missile_3.png"),
                (19, "graphics/two_face/missile/two_face_missile_4.png"),
                (24, "graphics/two_face/missile/two_face_missile_5.png")
            ],
            "combo3": [
                (4, "graphics/two_face/familiar/two_face_familiar_1.png"),
                (9, "graphics/two_face/familiar/two_face_familiar_2.png"),
                (14, "graphics/two_face/familiar/two_face_familiar_3.png"),
                (19, "graphics/two_face/familiar/two_face_familiar_4.png"),
                (24, "graphics/two_face/familiar/two_face_familiar_5.png")
            ],
            "combo4": [
                (4, "graphics/two_face/gunfire/two_face_gunfire_1.png"),
                (9, "graphics/two_face/gunfire/two_face_gunfire_2.png"),
                (14, "graphics/two_face/gunfire/two_face_gunfire_3.png"),
                (19, "graphics/two_face/gunfire/two_face_gunfire_4.png"),
                (24, "graphics/two_face/gunfire/two_face_gunfire_5.png")
            ]
        }