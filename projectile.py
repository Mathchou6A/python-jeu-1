import pygame
# from main import hauteur, largeur, screen # importer la largeur et la hauteur de l'écran

# definir la classe qui va gérer les projectiles de notre joueur
class projectile(pygame.sprite.Sprite):
   def __init__(self, player):
      super().__init__()
      self.image = pygame.image.load('assets/projectile.png')
      self.image = pygame.transform.scale(self.image, (50, 50))
      self.velocity = 6 # vitesse du projectile
      self.rect = self.image.get_rect()
      self.rect.x = player.rect.x + 140
      self.rect.y = player.rect.y + 90
      self.origin_image = self.image # sauvegarder l'image d'origine
      self.angle = 0 # angle de rotation
      self.player = player

   def rotate(self):
      self.angle += 5 # rotation de 5 degrés
      self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1) # faire tourner l'image
      self.rect = self.image.get_rect(center=self.rect.center)
   
   
   def remove(self):
      self.player.all_projectiles.remove(self)
      print("Projectile supprimé")



   def move(self):
      self.rect.x += self.velocity # deplacer le projectile vers la droite
      self.rotate() # faire tourner le projectile
      if self.rect.x > 1800: # si le projectile depasse la largeur de l'écran
         self.remove() # supprimer le projectile si il depasse la largeur de l'écran


