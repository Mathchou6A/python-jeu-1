
import pygame
pygame.init()


# créer une fenêtre de jeux
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Jeu pour l'anglais et la NSI")

background = pygame.image.load("assets/bg.jpg")



# boucle de jeu
running = True

while running:
   screen.blit(background, (0, 0)) # dessiner l'arrière-plan
   pygame.display.flip() # mettre à jour l'affichage
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
         pygame.quit()
         print("Fermeture du jeu")


