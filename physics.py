import numpy as np
from character import Character, StaticObject
from pygame import Surface
from typing import *

class PhysicsEngine:
    def __init__(self, gravity: float = -9.8, frame_rate = 60, ppm: int = 200):
        self.gravity: float = (gravity * ppm) / (frame_rate * frame_rate)
        self.characters: List[Character] = []
        self.statics: List[StaticObject] = []
        self.ambient: List = []
        self.background : StaticObject = None
        
    def addCharacter(self, character: Character, coordinates: Tuple[int, int]) -> int:
        self.characters.append(character)
        self.characters[-1].rect.bottomleft = coordinates
        return self.characters[-1]
        
    def setBackground(self, obj: StaticObject):
        self.background = obj
    
    def addAmbient(self, obj):
        self.ambient.append(obj)
    
    def isOnFloor(self, character: Character) -> Tuple[bool, int]:
        for i in range(len(self.statics)):
            if ((max(character.getRect().left, self.statics[i].getRect().left) <= 
                min(character.getRect().right, self.statics[i].getRect().right)) and
                character.getRect().bottom < self.statics[i].getRect().bottom and
                character.getRect().bottom > self.statics[i].getRect().top):
                character.getRect().bottom = self.statics[i].getRect().top + 5
                return True, i
        return False, -1
    
    def addStatic(self, obj: StaticObject) -> None:
        self.statics.append(obj)
    
    def update(self, keys_pressed) -> None:
        for i in range(len(self.characters)):
            self.characters[i].update(keys_pressed, self)
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
            if ((self.characters[i].rect.centerx <= 0 and self.characters[i].vel[0] < 0) or 
                (self.characters[i].rect.centerx >= 800 and self.characters[i].vel[0] > 0)):
                self.characters[i].vel[0] = 0
            self.characters[i].rect = self.characters[i].rect.move(self.characters[i].vel[0], self.characters[i].vel[1])
            
    def blitAll(self, screen: Surface) -> None:
        screen.blit(self.background.getImage(), self.background.getRect())
        for i in range(len(self.statics)):
            screen.blit(self.statics[i].getImage(), self.statics[i].getRect())
        for i in range(len(self.characters)):
            screen.blit(self.characters[i].getImg(), self.characters[i].getRect())
        for i in range(len(self.ambient)):
            self.ambient[i].display(screen)
