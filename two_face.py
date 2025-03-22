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
                (4, "graphics/two_face/missile/two_face_missile.png"),
                (9, "graphics/two_face/missile/two_face_missile.png"),
                (14, "graphics/two_face/missile/two_face_missile.png"),
                (19, "graphics/two_face/missile/two_face_missile.png"),
                (24, "graphics/two_face/missile/two_face_missile.png")
            ],
            "combo3": [
                (4, "graphics/two_face/familiar/two_face_familiar.png"),
                (9, "graphics/two_face/familiar/two_face_familiar.png"),
                (14, "graphics/two_face/familiar/two_face_familiar.png"),
                (19, "graphics/two_face/familiar/two_face_familiar.png"),
                (24, "graphics/two_face/familiar/two_face_familiar.png")
            ],
            "combo4": [
                (4, "graphics/two_face/gunfire/two_face_gunfire.png"),
                (9, "graphics/two_face/gunfire/two_face_gunfire.png"),
                (14, "graphics/two_face/gunfire/two_face_gunfire.png"),
                (19, "graphics/two_face/gunfire/two_face_gunfire.png"),
                (24, "graphics/two_face/gunfire/two_face_gunfire.png")
            ]
        }