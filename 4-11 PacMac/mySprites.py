"""
    Author: < Your Name Here >
    
    Date: May 11, 2022
    
    Description: Cherry, PacMan, and ScoreKeeper subclasses for PacMan game
"""

import pygame
import random

# 1. ADD YOUR "Cherry" CLASS HERE...
class Cherry(pygame.sprite.Sprite):
    '''Sprite subclass for Cherry sprites.'''
    def __init__(self, screen):
        '''Initializer to set the image for our Cherry Sprite.'''        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the cherries
        self.image = pygame.image.load("Cherry.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())    


# 3. COMPLETE THE "PacMan" CLASS BELOW...
class PacMan(pygame.sprite.Sprite):
    '''Sprite subclass for user-controlled PacMan sprite.'''
    def __init__(self, screen):
        '''Initializer to set the image for our Circle Sprite.'''        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Unique instance variables for 4 PacMan images
        self.up_image = pygame.image.load("Up.png")
        self.down_image = pygame.image.load("Down.png")
        self.left_image = pygame.image.load("Left.png")
        self.right_image = pygame.image.load("Right.png")

        # Unique instance variables for the window and x & y directions
        self.window = screen
        self.dir_x = 0
        self.dir_y = 0

        # Start with right_image, centered in window
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() // 2
        self.rect.centery = screen.get_height() //2         
        
    def goRight(self):
        '''Make PacMan move RIGHT, and change to right_image'''
        self.image = self.right_image
        self.dir_y = 0
        self.dir_x = 5

    def goLeft(self):
        '''Make PacMan move LEFT, and change to left_image'''
        self.image = self.left_image
        self.dir_y = 0
        self.dir_x = -5
        
    def goUp(self):
        '''Make PacMan move UP, and change to up_image'''
        self.image = self.up_image
        self.dir_x = 0
        self.dir_y = -5
        
    def goDown(self):
        '''Make PacMan move DOWN, and change to down_image'''
        self.image = self.down_image
        self.dir_x = 0
        self.dir_y = 5
    
    def update(self):
        '''Update location of PacMan, make him reappear on 
        opposite side of the window if he goes beyond window edge'''
        self.rect.centerx += self.dir_x
        if self.rect.left > self.window.get_width():
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = self.window.get_width()
        
        self.rect.centery += self.dir_y
        if self.rect.top > self.window.get_height():
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = self.window.get_height()

class ScoreKeeper(pygame.sprite.Sprite):
    '''Sprite subclass ScoreKeeper to display the current points'''
    def __init__(self):
        '''Initializer to set the font and score for our Sprite.'''        
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 40)
        self.points = 0
        
    def addPoint(self):
        '''Add a point to the score to be displayed.'''
        self.points += 1
        
    def getPoints(self):
        '''Accessor to return current number of points'''
        return self.points
                
    def update(self):
        '''Render and center the scorekeeper text on each Refresh.'''
        self.image = self.font.render("Score: " + str(self.points), 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 320
        self.rect.centery = 30
