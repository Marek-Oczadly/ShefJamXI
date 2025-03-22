import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.image = pygame.transform.scale_by(self.image, 0.25)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp

    # make it move, given array of keys
    def move(self, direction):
        self.rect = self.rect.move(direction, 0)

    # make it jump, given array of keys
    def jump(self, keys):
        pass

    # first combo, should be defined in subclass
    def combo1(self, keys):
        pass

    def setRect(self, new_file: str):
        self.image = pygame.image.load(new_file).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, keys):

        if keys[pygame.K_a]:
            self.move(-5)
        if keys[pygame.K_d]:
            self.move(5)
    
    def getImg(self):
        return self.image
    
    def getRect(self):
        return self.rect
