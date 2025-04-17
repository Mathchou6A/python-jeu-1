import pygame

# créer une classe qui va gérer les monstres
class Monster(pygame.sprite.Sprite):
   def __init__(self, game):
      super().__init__()
      self.game = game
      self.image = pygame.image.load("assets/mummy.png")  
      self.rect = self.image.get_rect()
      self.max_health = 100
      self.health = 100 
      self.attack = 5 
      self.rect.x = 1430 # position x du monstre
      self.rect.y = 450 # position y du monstre
      self.velocity = 2 # vitesse du monstre

   def forward(self):
      # le déplacement ne se fait que si le monstre n'est pas en collision avec un groupe de joueurs
      if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity


