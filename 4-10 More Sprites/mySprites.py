"""
    Author: < Your Name Here >
    
    Date: May 10, 2022
    
    Description: A Collection Of Useful Sprite Classes
"""
"""
    YOUR TASKS:
    
    1. Modify the Brick class so that each Brick sprite starts at a random 
       location in the game window, but then moves in a random x & y direction
       until it hits the edge of the game window.  Hints: The update() method 
       should check if the Brick has hit an edge of the game window.   If it 
       hits the left or right of the window, reverse the x direction.   If it
       hits the top or bottom, reverse the y direction.
       
    2. Modify the main() code below to demo your revised Brick class but
       change the number of Brick sprites to *25*.   Observe what happens 
       when Brick sprites collide with each other.  We'll talk about detecting
       such collisions next time!  Try *1000* brick sprites, just for fun!
       
    3. Modify the Circle class such that you can specify the (R,G,B) colour as
       a tuple (R,G,B) parameter to its __init__() method.   Modify main() to 
       include a Circle sprite in addition to all of the flying Brick sprites.
       Generate a random RGB colour when to instantiate your Circle.  Use the 
       pygame.mouse.set_visible() method to hide the mouse pointer.
       
    4. Modify the Label class such that you can specify the message, 
       x_y_center, font_name, size, and (R,G,B) colour as parameters to the
       __init__() method.   Modify main() to demonstrate your revised Label sprite.
"""
import pygame
import random

class Brick(pygame.sprite.Sprite):
    '''A simple Sprite subclass to represent static Brick sprites.'''
    def __init__(self, screen, xdir, ydir):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # Set the image and rect attributes for the bricks
        self.image = pygame.image.load("bricks.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, screen.get_width())
        self.rect.centery = random.randrange(0, screen.get_height())    
        self.xdir = xdir
        self.ydir = ydir

    def update(self):
        '''Move the brick in a random x and y direction until it hits the edge of the screen.'''
        self.rect.centerx += self.xdir
        if (self.rect.left < 0) or (self.rect.right > 640):
            self.xdir = -self.xdir

        self.rect.centery += self.ydir
        if (self.rect.top < 0) or (self.rect.bottom > 480):
            self.ydir = -self.ydir


class Circle(pygame.sprite.Sprite):
    '''Mouse-following Circle Sprite subclass.'''
    def __init__(self, color: tuple):
        '''Initializer to set the image for our Circle Sprite.''' 

        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)

        # create circle
        self.image = pygame.Surface((50, 50))
        self.image = self.image.convert()

        # draw circle, with transparent alpha background
        pygame.draw.circle(self.image, color, (25, 25), 25)
        self.image.set_colorkey((0, 0, 0))

        
        

        # set color
        self.color = color

        # set rect
        self.rect = self.image.get_rect()

        
        
    def update(self):
        '''Move the center of the circle to where the mouse is pointing.'''
        self.rect.center = pygame.mouse.get_pos()

        
class Label(pygame.sprite.Sprite):
    '''A mutatable text Label Sprite subclass'''
    def __init__(self, message, x_y_center, font_name, size, color):
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont(font_name, size)
        self.text = message
        self.color = color
        # set color
        self.image = self.font.render(self.text, 1, self.color)
        self.center = x_y_center
        
    def setText(self, message):
        '''Change the text of the label'''
        self.text = message
    
    def update(self):
        '''Update the text of the label'''
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.center
        
