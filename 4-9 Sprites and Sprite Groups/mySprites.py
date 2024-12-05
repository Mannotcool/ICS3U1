"""
    Author: Nick S
    
    Date: Dec 3rd 2024
    
    Description: A module containing my custom Box subclass of Sprite.
"""

import pygame
import random

class Box(pygame.sprite.Sprite):
    '''Our Box class inherits from the Sprite class'''
    def __init__(self, screen, x, y, xdir, ydir, r, g, b):
        '''Initializer to set the image, position, 
        and direction for a Box Sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        
        # Keep track of the screen so we can call get_witdth()
        self.window = screen
        
        # Define a red Surface for our Box Sprite
        self.image = pygame.Surface((25, 25))
        self.image = self.image.convert()
        self.image.fill((r, g, b))
        
        # Define the position of our Box using it's rect
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.xdir = xdir
        self.ydir = ydir

    def update(self):
        '''This method is called automatically in the Refresh 
        section to pdate our Box Sprite's position.'''
        self.rect.left += self.xdir
        if (self.rect.left < 0) or (self.rect.right > self.window.get_width()):
            self.xdir = -self.xdir

        self.rect.top += self.ydir
        if (self.rect.top < 0) or (self.rect.bottom > self.window.get_height()):
            self.ydir = -self.ydir

        
