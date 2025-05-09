import pygame
import random
import animation

# créer une classe qui va gérer les monstres
class Monster(animation.AnimateSprite):
   def __init__(self, game, name, size, offset=0):
      super().__init__(name, size)
      self.game = game
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100
      self.attack = 0.3
      self.rect.x = 1550 + random.randint(0, 500) # position x du monstre
      self.rect.y = 450 - offset # position y du monstre
      self.start_animation()
      self.loot_amount = 10
   
   
   def set_speed(self, speed):
      self.default_speed = speed # vitesse par défaut du monstre
      self.velocity = random.randint(1, speed) # vitesse du monstre
   
   
   def set_loot_amount(self, amount):
      self.loot_amount = amount
   
   
   def damage(self, damage):
      # infliger des dégâts au monstre
      self.health -= damage
      # vérifier si sont nouveau de vie est inférieur ou égal à 0
      if self.health <= 0:
         # reapparaitre comme un nouveau monstre
         self.health = self.max_health
         self.rect.x = 1550 + random.randint(0, 500)
         self.velocity = random.randint(1, self.default_speed) # réinitialiser la vitesse du monstre
         
         # ajouter le nombre de poits score
         self.game.add_score(self.loot_amount) # ajouter 1 point de score
         
         # si la bar d'evenement est chagé a son max
         if self.game.comet_event.is_full_loaded():
            # retirer du jeu
            self.game.all_monsters.remove(self) # supprimer le monstre du groupe de monstres
            print("monstre mort")
            # appeler la fonction pour essayer de faire tomber la comète
            self.game.comet_event.attempt_fall()  
   
   def update_animation(self):
      self.animate() # si on veux que l'animation du monstre reste en boucle : self.animate(loop=True)
   
   def update_health_bar(self, surface):
      # dessiner l'arrière-plan de la barre de vie
      pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
      # dessiner la barre de vie
      pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])


   def forward(self):
      # le déplacement ne se fait que si le monstre n'est pas en collision avec un groupe de joueurs
      if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity
         self.start_animation() # démarrer l'animation
      else:
         # infliger des dégâts au joueur
         self.game.player.damage(self.attack)


# définir une classe pour la momie
class Mummy(Monster):
   def __init__(self, game):
      super().__init__(game, 'mummy', (130, 130))
      self.set_speed(6) # vitesse de la momie
      self.set_loot_amount(20)

# def une classe pour l'alien
class Alien(Monster):
   def __init__(self, game):
      super().__init__(game, 'alien', (300, 300), offset=140)
      self.health = 250
      self.max_health = 250
      self.attack = 1
      self.set_speed(4) # vitesse de l'alien
      self.set_loot_amount(80)


