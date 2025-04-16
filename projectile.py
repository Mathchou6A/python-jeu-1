import pygame

# definir la classe qui va gérer les projectiles de notre joueur
class projectile(pygame.sprite.Sprite):
   def __init__(self, player):
      super().__init__()
      self.image = pygame.image.load('assets/projectile.png')
      self.image = pygame.transform.scale(self.image, (50, 50))
      self.velocity = 5
      self.rect = self.image.get_rect()
      self.rect.x = player.rect.x + 140
      self.rect.y = player.rect.y + 90

