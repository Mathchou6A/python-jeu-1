
import pygame
pygame.init()

# creer une preière classe qui va representer le joueur
class player(pygame.sprite.Sprite):
   def __init__(self):
      super().__init__()
      self.health = 100
      self.max_health = 100
      self.attack = 10
      self.velocity = 5
      self.image = pygame.image.load('assets/player.png')
      self.rect = self.image.get_rect()


# créer une fenêtre de jeux
screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/bg.jpg") # charger l'arrière-plan

player = player() # charger notre player


# boucle de jeu
running = True

while running:
   screen.blit(background, (-600, 0)) # dessiner l'arrière-plan
   pygame.display.flip() # mettre à jour l'affichage
   screen.blit(player.image, player.rect) #appeler l'image du joueur
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")


