
import pygame
from game import game # importer notre jeu
pygame.init()


# créer une fenêtre de jeux
screen = pygame.display.set_mode((1550, 700)) # définir la taille de la fenêtre   (1800, 950)
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/bg.jpg") # charger l'arrière-plan

game = game() # charger notre jeu


# boucle de jeu
running = True

while running:
   screen.blit(background, (-850, -300)) # dessiner l'arrière-plan (-600, -100)
   screen.blit(game.player.image, game.player.rect) #appeler l'image du joueur
   if game.perssed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width(): # si la touche droite est enfoncée
      game.player.move_right() # déplacer le joueur vers la droite   
   elif game.perssed.get(pygame.K_q) and game.player.rect.x > -30: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran
      game.player.move_left() # déplacer le joueur vers la gauche
   print(game.player.rect.x) # afficher la position du joueur
      
      
      
      
      
      
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")
      elif event.type == pygame.KEYDOWN: # si une touche est enfoncée
         game.perssed[event.key] = True
      elif event.type == pygame.KEYUP: # si une touche est relâchée
         game.perssed[event.key] = False







