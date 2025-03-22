import pygame
from character import Character

class TwoFace(Character):
    def __init__(self, player_name, max_hp, base_image):
        super().__init__(player_name, max_hp, base_image)

    def combo1(self):
        frame_data = [
            (4, "graphics/two_face/attack1/two_face_blast_1.png"),
            (9, "graphics/two_face/attack1/two_face_blast_2.png"),
            (14, "graphics/two_face/attack1/two_face_blast_3.png"),
            (19, "graphics/two_face/attack1/two_face_blast_4.png"),
            (24, "graphics/two_face/attack1/two_face_blast_5.png")
        ]
        self.setComboFrame(self.frame, frame_data)