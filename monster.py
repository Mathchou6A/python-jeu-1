import pygame

# créer une classe qui va gérer les monstres
class Monster(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('assets/monster.png')
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 5