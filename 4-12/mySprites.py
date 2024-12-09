import pygame

class Box(pygame.sprite.Sprite):
    '''Our Joystick-controlled Box Sprite'''
    def __init__(self, screen, x_pos):
        '''Initializer to set the image, position, and direction for a Box Sprite.'''
        # Call the parent __init__() method
        pygame.sprite.Sprite.__init__(self)
          
        # Keep track of the screen so we can call get_witdth()
        self.window = screen
         
        # Define a black Surface for our Box Sprite
        self.image = pygame.Surface((40, 40))
        self.image = self.image.convert()
        self.image.fill((0, 0, 0))
          
        # Set the rect for our Box sprite, as well as direction (dx & dy)
        self.rect = self.image.get_rect()
        self.rect.left = x_pos
        self.rect.top = 200
        self.dx = 0
        self.dy = 0
   
    def changeColour(self, button_num):
        '''Depending on the joystick button_num (0 -> 11) pressed, 
        an RGB colour tuple is chosen from a list of colours to 
        change the colour of our Box sprite.'''
        colours = [ (0,0,0),(0,0,111),(0,111,0),(0,111,111), \
                    (111,0,0),(111,0,111),(111,111,0),(111,111,111),\
                    (0,0,222),(0,222,0),(222,0,0),(222,222,222) ]
        self.image.fill(colours[button_num])
      
    def changeDirection(self, xy_change):
        '''xy_change is an (x,y) tuple used to change the dx and dy
        directions for our Box sprite.'''
        self.dx, self.dy = xy_change
          
    def update(self):
        '''Move the Box each frame, but keep within window boundaries.'''       
        if ((self.rect.left > 0) and (self.dx < 0)) or\
           ((self.rect.right < self.window.get_width()) and\
           (self.dx > 0)):
            self.rect.left += (self.dx*5)
        if ((self.rect.top > 0) and (self.dy > 0)) or\
           ((self.rect.bottom < self.window.get_height()) and\
           (self.dy < 0)):
            self.rect.top -= (self.dy*5)