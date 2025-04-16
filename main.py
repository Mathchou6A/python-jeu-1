
import pygame
from game import game # importer notre jeu
pygame.init()


# créer une fenêtre de jeux
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/bg.jpg") # charger l'arrière-plan

game = game() # charger notre jeu


# boucle de jeu
running = True

while running:
   screen.blit(background, (0, -200)) # dessiner l'arrière-plan
   screen.blit(game.player.image, game.player.rect) #appeler l'image du joueur
   
   
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")








