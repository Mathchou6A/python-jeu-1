import pygame
from projectile import projectile # importer notre projectile

# creer une preière classe qui va representer le joueur
class player(pygame.sprite.Sprite):
   def __init__(self, game):
      super().__init__()
      self.game = game
      self.image = pygame.image.load('assets/player.png')
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 10
      self.velocity = 5
      self.all_projectiles = pygame.sprite.Group()
      self.rect.x = 400
      self.rect.y = 400
   
   
   def damage(self, damage):
      if self.health - damage > damage:
         self.health -= damage

      if self.health <= 0:
         # reapparaitre comme un nouveau joueur
         self.health = self.max_health
         self.rect.x = 400
         self.rect.y = 400
         
         
   
   def update_health_bar(self, surface):
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])   
      
   def launch_projectile(self):       # lancer un projectile
      self.all_projectiles.add(projectile(self))

   def move_right(self):
      # si le joueur n'est pas en colision avec un monstre
      if not self.game.check_collision(self, self.game.all_monsters):
         self.rect.x += self.velocity
      
   def move_left(self):
      self.rect.x -= self.velocity



