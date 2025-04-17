
import pygame
from game import game # importer notre jeu
pygame.init()


# largeur de la fenêtre
largeur = 1550
# hauteur de la fenêtre
hauteur = 700

# créer une fenêtre de jeux
screen = pygame.display.set_mode((largeur, hauteur)) # définir la taille de la fenêtre   (1800, 950)
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/bg.jpg") # charger l'arrière-plan

game = game() # charger notre jeu


# boucle de jeu
running = True


while running:
   # print(screen.get_width())
   # print(screen.get_height())
   # appliquer l'image de fond
   screen.blit(background, (-850, -300)) 
   
   #appliquer l'image du joueur
   screen.blit(game.player.image, game.player.rect) 
   
   # actualiser la barre de vie du joueur
   game.player.update_health_bar(screen) # mettre à jour la barre de vie du joueur
   
   #récupérer tous les projectiles du joueur
   for projectile in game.player.all_projectiles:
      projectile.move()
   
   #appeler l'image du projectile
   game.player.all_projectiles.draw(screen) # dessiner tous les projectiles du joueur
   
   # appliquer l'ensemble des images de mon groupe de monstres
   game.all_monsters.draw(screen) # dessiner tous les monstres
   
   # recuperer tous les monstres du groupe de monstres
   for monster in game.all_monsters:
      monster.forward() # faire avancer le monstre
      monster.update_health_bar(screen) # mettre à jour la barre de vie du monstre
   
   
   # verifier si le joueur soit aller à gauche ou à droite
   if game.perssed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width(): # si la touche droite est enfoncée
      game.player.move_right() # déplacer le joueur vers la droite   
   elif game.perssed.get(pygame.K_q) and game.player.rect.x > -30: # si la touche gauche est enfoncée et que le joueur ne dépace pas la gauche de l'écran
      game.player.move_left() # déplacer le joueur vers la gauche
      
      
      
      
      
      
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")
      elif event.type == pygame.KEYDOWN: # si une touche est enfoncée
         game.perssed[event.key] = True
         
         # decaler si la touche z est enfoncée pour lancer un projectile
      # Déclenchement avec un clic gauche de souris
      elif event.type == pygame.MOUSEBUTTONDOWN:
         if event.button == 1:  # 1 = bouton gauche
            game.player.launch_projectile()
      
      elif event.type == pygame.KEYUP: # si une touche est relâchée
         game.perssed[event.key] = False







