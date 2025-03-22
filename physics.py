import numpy as np
import character
from pygame import Surface
from typing import *

class PhysicsEngine:
    def __init__(self, gravity: float = -9.8, frame_rate = 60, ppm: int = 200):
        self.gravity: float = (gravity * ppm) / (frame_rate * frame_rate)
        self.characters: List[character.Character] = []
        self.statics: List[character.StaticObject] = []
        
    def init(self) -> None:
        for i in range(len(self.statics)):
            self.statics[i].init()
        
    def addCharacter(self, character: character.Character) -> None:
        self.characters.append(character)
        
    def isOnFloor(self, character: character.Character) -> Tuple[bool, int]:
        for i in range(len(self.statics)):
            if ((max(character.getRect().left, self.statics[i].getRect().left) <= 
                min(character.getRect().right, self.statics[i].getRect().right)) and
                character.getRect().bottom < self.statics[i].getRect().bottom and
                character.getRect().bottom > self.statics[i].getRect().top):
                print("Reached")
                return True, i
        return False, -1
    
    def addStatic(self, obj: character.StaticObject) -> None:
        self.statics.append(obj)
    
    def update(self, keys_pressed) -> None:
        for i in range(len(self.characters)):
            self.characters[i].update(keys_pressed)
            if not self.isOnFloor(self.characters[i])[0]:
                self.characters[i].acc[1] = -self.gravity
            else:
                self.characters[i].acc[1] = min(0, self.characters[i].acc[1])
                self.characters[i].vel[1] = min(0, self.characters[i].vel[1])
            if not self.characters[i].vel[0] == 0 :
                if self.isOnFloor(self.characters[i])[0]:
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
        for i in range(len(self.statics)):
            screen.blit(self.statics[i].getImage(), self.statics[i].getRect())
        for i in range(len(self.characters)):
            screen.blit(self.characters[i].getImg(), self.characters[i].getRect())
