import pygame

class Character(pygame.sprite.Sprite):

    def __init__(self, player_name: str, max_hp: int, height: int, width: int, base_image: str):
        pygame.sprite.Sprite.__init__(self) 
  
        self.image = pygame.image.load(base_image)
        self.rect = self.image.get_rect()
        self.player_name = player_name
        self.max_hp = max_hp

    # make it move, given array of keys
    def move(keys):
        pass

    # make it jump, given array of keys
    def jump(keys):
        pass

    # first combo, should be defined in subclass
    def combo1(keys):
        pass