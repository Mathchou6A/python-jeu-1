import pygame
import random

# créer une classe qui va gérer les monstres
class Monster(pygame.sprite.Sprite):
   def __init__(self, game):
      super().__init__()
      self.game = game
      self.image = pygame.image.load("assets/mummy.png")  
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 0.3
      self.rect.x = 1550 + random.randint(0, 500) # position x du monstre
      self.rect.y = 450 # position y du monstre
      self.velocity = random.randint(1, 3) # vitesse du monstre
   
   def damage(self, damage):
      # infliger des dégâts au monstre
      self.health -= damage
      # vérifier si sont nouveau de vie est inférieur ou égal à 0
      if self.health <= 0:
         # reapparaitre comme un nouveau monstre
         self.health = self.max_health
         self.rect.x = 1550 + random.randint(0, 500)
         self.velocity = random.randint(1, 3)
   
   
   def update_health_bar(self, surface):
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


   def forward(self):
      # le déplacement ne se fait que si le monstre n'est pas en collision avec un groupe de joueurs
      if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity
      else:
         # infliger des dégâts au joueur
         self.game.player.damage(self.attack)


