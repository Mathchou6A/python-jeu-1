import pygame
from comet import Comet # importer notre comète


# créer une classe pour gérer cet événement
class CometFallEvent:
   def __init__(self, game):
      self.percent = 0
      self.percent_speed = 7
      self.game = game
      self.fall_mode = False
      
      # définir un groupe spraite pour les comètes
      self.all_comets = pygame.sprite.Group()
   
   
   def add_percent(self):
      self.percent += self.percent_speed / 100
   
   def is_full_loaded(self):
      return self.percent >= 100
   
   def reset_percent(self):
      self.percent = 0
   
   def meteor_fall(self):
      # apparaitre 1 première comète
      self.all_comets.add(Comet(self))
   
   def attempt_fall(self):
      # la jauge d'evénement est pleine
      if self.is_full_loaded() and len(self.game.all_monsters) == 0:
         # si la barre d'événement est pleine, on fait tomber la comète
         print("pluie de comète !!")
         self.meteor_fall() # ajouter une comète à notre groupe de comètes
         self.fall_mode = True # activer le mode de chute de comète
   
   def update_bar(self, surface):
      #ajouter 1% à la barre d'événement
      self.add_percent()
      

      
      # barre noir (en arrière plan)
      pygame.draw.rect(surface, (0, 0, 0), [
         0, # l'axe des x
         surface.get_height() - 30, # l'axe des y
         surface.get_width(), # la largeur de la barre
         10 # epaisseur de la barre
      ])
      # barre rouge (avant plan)
      pygame.draw.rect(surface, (187, 11, 11), [
         0, # l'axe des x
         surface.get_height() - 30, # l'axe des y
         (surface.get_width() / 100) * self.percent, # la largeur de la barre
         10 # epaisseur de la barre
      ])

         
         
         
         
         
         
      