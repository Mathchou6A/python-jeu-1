import pygame
from projectile import projectile # importer notre projectile
import animation

# creer une preière classe qui va representer le joueur
class player(animation.AnimateSprite):
   def __init__(self, game):
      super().__init__('player')
      self.game = game
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
      else:
         # si la vie du joueur est inférieure à 0, il meurt
         self.game.game_over()
   
   
   def update_animation(self):
      # mettre à jour l'animation du joueur
      self.animate()   
   
   def update_health_bar(self, surface):
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])   
      
   def launch_projectile(self):       # lancer un projectile
      self.all_projectiles.add(projectile(self))
      # démarrer l'animation 
      self.start_animation()
      self.game.sound_manager.play('tir')

   def move_right(self):
      # si le joueur n'est pas en colision avec un monstre
      if not self.game.check_collision(self, self.game.all_monsters):
         self.rect.x += self.velocity
      
   def move_left(self):
      self.rect.x -= self.velocity



