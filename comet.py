import pygame
import random


# créer une classe pour gérer les comètes
class Comet(pygame.sprite.Sprite):
   def __init__(self, comet_event):
      super().__init__()
      # def l'image de la comète
      self.image = pygame.image.load('assets/comet.png')
      self.rect = self.image.get_rect()
      self.velocity = random.randint(1, 3)
      self.rect.x = random.randint(-30, 1500) # position x aléatoire
      self.rect.y = - random.randint(0, 800) # position y aléatoire
      self.comet_event = comet_event # l'événement de la comète
   
   def remove(self):
      self.comet_event.all_comets.remove(self) # supprimer la comète du groupe de comètes
      
      # verifier si le nombre de comètes est égal à 0
      if len(self.comet_event.all_comets) == 0:
         print("l'événement de comète est terminé")
         # remettre la barre d'événement à 0
         self.comet_event.reset_percent()
         # apparaitre les 2 premier monstres
         self.comet_event.game.spawn_monster()
         self.comet_event.game.spawn_monster()
   
   def fall_comet(self):
      # faire tomber la comète
      self.rect.y += self.velocity
      
      # si la comète touche le sol, elle disparait
      if self.rect.y > 430:
         print("comète disparue")
         self.remove() # supprimer la comète
         
         # si il n'y a plus de boule de feu
         if len(self.comet_event.all_comets) == 0:
            print("l'événement de comète est terminé")
            # remettre la barre d'événement à 0
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False
      
      # si la comète touche un joueur, elle inflige des dégats au joueur
      if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
         # infliger des dégats au joueur
         print("joueur touché par la comète")
         # suppression de la comète
         self.remove() 
         # subir 20 points de dégats
         self.comet_event.game.player.damage(20)