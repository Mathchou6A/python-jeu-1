import pygame
from player import player # importer notre joueur
from monster import Monster # importer notre monstre

# créer une classe qui va représenter notre jeu
class game:
   def __init__(self):
      # generer notre joueur
      self.player = player()
      
      #groupe de monsetres
      self.all_monsters = pygame.sprite.Group()      
      self.perssed = {}
      self.spawn_monster() # faire spawn un monstre
      
   def spawn_monster(self):
      monster = Monster()
      self.monster.rect.x = 800
      self.all_monsters.add(monster) # ajouter le monstre au groupe de monstres


