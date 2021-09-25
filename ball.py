import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        self.screen_rect = ai_game.screen.get_rect()
        
        # self.image = pygame.image.load('images/rocket_small.png')
        self.image = pygame.image.load('images/ship.bmp')
 
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()

        
        
        self.rect.x = self.rect.width
        self.rect.x = self.rect.width
        
        self.y = float(self.rect.x)
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += 0.3
        # Update the rect position.
        self.rect.y = self.y

