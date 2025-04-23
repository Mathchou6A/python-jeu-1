import pygame

# définir une class qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):
   # définir les hcauses a faire à la création de l'entité
   def __init__(self, sprite_name, size=(200, 200)):
      super().__init__()
      self.size = size # la taille de l'image
      self.image = pygame.image.load(f'assets/{sprite_name}.png')
      self.image = pygame.transform.scale(self.image, size) # redimensionner l'image
      self.current_image = 0 # l'image actuelle
      self.images = animations.get(sprite_name) # la liste des images
      self.animation = False
   
   # def une méthode pour démarrer l'animation
   def start_animation(self, loop=False):
      self.animation = True
   
   
   # def une méthode pour animer le sprite
   def animate(self):
      
      # verifier si l'animation est activée
      if self.animation:
         # passer à l'image suivante
         self.current_image += 1
         
         #verifier si on a atteint la dernière image
         if self.current_image >= len(self.images):
            # remettre l'image actuelle à 0
            self.current_image = 0
            
            # vérifier si l'animation doit être en boucle
            # if loop == False:
               # self.animation = False # désactiver l'animation
            
            self.animation = False # désactiver l'animation
         
         
         # modif l'image précédente par la suivante
         self.image = self.images[self.current_image]
         self.image = pygame.transform.scale(self.image, self.size)
   
# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
   # charger les 24 images de ce sprite dans le dossier correspondant
   images = []
   # récupérer le chemin du dossier pour ce sprite
   path = f'assets/{sprite_name}/{sprite_name}'
   
   # boucler sur charque image dans ce dossier
   for num in range(1, 25):
      image_path = path + str(num) + '.png'
      pygame.image.load(image_path)
      images.append(pygame.image.load(image_path))
   
   # renvoyer le contenu de la liste dimages
   return images

# def un dico qui va contenir les image chargées de chaque sprite
# mummy -> [...mummy1.png, mummy2.png, ...]
# player -> [...player1.png, player2.png, ...]
# charger les images de chaque sprite
animations = {
   'mummy': load_animation_images('mummy'),
   'player': load_animation_images('player'),   
   'alien': load_animation_images('alien'),
}
