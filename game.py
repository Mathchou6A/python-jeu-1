from player import player # importer notre joueur
from monster import Alien, Monster, Mummy # importer notre monstre
from comet_event import CometFallEvent
import pygame

# créer une classe qui va représenter notre jeu
class game:
   def __init__(self):
      # def si notre jeu a comancé
      self.is_playing = False
      # generer notre joueur
      self.all_players = pygame.sprite.Group()
      self.player = player(self)
      self.all_players.add(self.player)
      # générer l'évenement 
      self.comet_event = CometFallEvent(self)
      
      #groupe de monstres
      self.all_monsters = pygame.sprite.Group()
      self.perssed = {}

   
   def start(self):
      self.is_playing = True
      self.spawn_monster(Mummy)
      self.spawn_monster(Mummy)
      self.spawn_monster(Alien)
   
   def game_over(self):
      self.all_monsters = pygame.sprite.Group() # vider le groupe de monstres
      self.comet_event.all_comets = pygame.sprite.Group() # vider le groupe de comètes
      self.comet_event.reset_percent() # remettre la barre d'événement à 0
      self.player.health = self.player.max_health # remettre la vie du joueur à 100
      self.is_playing = False # remettre le jeu en attente
      

      
   def update(self, screen):
      #appliquer l'image du joueur
      screen.blit(self.player.image, self.player.rect) 
      
      # actualiser la barre de vie du joueur
      self.player.update_health_bar(screen) # mettre à jour la barre de vie du joueur
      
      # actualiser la barre d'evenement du jeu
      self.comet_event.update_bar(screen) # mettre à jour la barre d'événement
      
      # actualiser l'animation du joueur
      self.player.update_animation()
      
      #récupérer tous les projectiles du joueur
      for projectile in self.player.all_projectiles:
         projectile.move()
      
      # recuperer tous les monstres du groupe de monstres
      for monster in self.all_monsters:
         monster.forward() # faire avancer le monstre
         monster.update_health_bar(screen) # mettre à jour la barre de vie du monstre
         monster.update_animation() # mettre à jour l'animation du monstre
      
      # récupérerles les comets de notre jeu
      for comet in self.comet_event.all_comets:
         comet.fall_comet()
      
      #appeler l'image du projectile
      self.player.all_projectiles.draw(screen) # dessiner tous les projectiles du joueur
      
      # appliquer l'ensemble des images de mon groupe de monstres
      self.all_monsters.draw(screen) # dessiner tous les monstres
      
      # appliquer l'ensemble des images de mon groupe de comètes
      self.comet_event.all_comets.draw(screen)
      
      # verifier si le joueur soit aller à gauche ou à droite
      if self.perssed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width(): # si la touche droite est enfoncée
         self.player.move_right() # déplacer le joueur vers la droite   
      elif self.perssed.get(pygame.K_q) and self.player.rect.x > -30: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran
         self.player.move_left() # déplacer le joueur vers la gauche
   
   
   def check_collision(self, sprite, group):
      return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask) # vérifier si le joueur touche un monstre
   
   def spawn_monster(self, monster_class_name):
      self.all_monsters.add(monster_class_name.__call__(self)) # ajouter le monstre à notre groupe de monstres




