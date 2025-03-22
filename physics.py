import numpy as np
import character
from pygame import Surface
from typing import *

class PhysicsEngine:
    def __init__(self, gravity: float = -9.8, frame_rate = 60, ppm: int = 200):
        self.gravity: float = (gravity * ppm) / (frame_rate * frame_rate)
        self.characters: List[character.Character] = []
        
    def addCharacter(self, character: character.Character) -> None:
        self.characters.append(character)
    
    def update(self, keys_pressed) -> None:
        for i in range(len(self.characters)):
            self.characters[i].update(keys_pressed)
            if not self.characters[i].isOnFloor():
                self.characters[i].acc[1] = -self.gravity
            else:
                self.characters[i].acc[1] = min(0, self.characters[i].acc[1])
                self.characters[i].vel[1] = min(0, self.characters[i].vel[1])
            if not self.characters[i].vel[0] == 0 :
                if self.characters[i].isOnFloor():
                    self.characters[i].acc[0] = self.characters[i].vel[0] / abs(self.characters[i].vel[0]) * -0.5
                else:
                    self.characters[i].acc[0] = self.characters[i].vel[0] / abs(self.characters[i].vel[0]) * -0.05
                if ((self.characters[i].vel[0] < 0 and -self.characters[i].acc[0] < self.characters[i].vel[0]) or
                    (self.characters[i].vel[0] > 0 and -self.characters[i].acc[0] > self.characters[i].vel[0])):
                    self.characters[i].acc[0] = 0
                    self.characters[i].vel[0] = 0
            self.characters[i].vel += self.characters[i].acc
            self.characters[i].rect = self.characters[i].rect.move(self.characters[i].vel[0], self.characters[i].vel[1])
            
    def blitAll(self, screen: Surface) -> None:
        for i in range(len(self.characters)):
            screen.blit(self.characters[i].getImg(), self.characters[i].getRect())