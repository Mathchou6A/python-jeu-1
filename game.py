from player import player # importer notre joueur
from monster import Monster # importer notre monstre
import pygame

# créer une classe qui va représenter notre jeu
class game:
   def __init__(self):
      # generer notre joueur
      self.all_players = pygame.sprite.Group()
      self.player = player(self)
      self.all_players.add(self.player)
      
      #groupe de monstres
      self.all_monsters = pygame.sprite.Group()
      self.perssed = {}
      self.spawn_monster()

   def check_collision(self, sprite, group):
      return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # vérifier si le joueur touche un monstre

   def spawn_monster(self):
      monster = Monster(self) # créer un monstre
      self.all_monsters.add(monster) # ajouter le monstre à notre groupe de monstres




