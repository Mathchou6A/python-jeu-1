import pygame
from projectile import projectile # importer notre projectile

# creer une preière classe qui va representer le joueur
class player(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.image = pygame.image.load('assets/player.png')
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 10
      self.velocity = 5
      self.all_projectiles = pygame.sprite.Group()
      self.rect.x = 400
      self.rect.y = 400
      
      
   def launch_projectile(self):       # lancer un projectile
      self.all_projectiles.add(projectile(self))

   def move_right(self):
      self.rect.x += self.velocity
      
   def move_left(self):
      self.rect.x -= self.velocity



