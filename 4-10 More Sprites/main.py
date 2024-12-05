"""
    Author: < Your Name Here >
    
    Date: May 10, 2022
    
    Description: Demonstrating the Bricks, Circle, and Label Sprites!
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
import mySprites
import random

def main():
   '''This function defines the 'mainline logic' for our game.'''
   # Initialize pygame
   pygame.init()

   # hide mouse pointer
   pygame.mouse.set_visible(False)
   
   # Display
   screen = pygame.display.set_mode((640, 480))
   pygame.display.set_caption("Lots of Sprites!")
    
   # Entities
   background = pygame.Surface(screen.get_size())
   background.fill((255, 255, 255))
   screen.blit(background, (0, 0))

   # Create 10 random bricks using a loop and a list
   bricks = []
   for i in range(25):
      bricks.append(mySprites.Brick(screen, random.choice([-1, 1]), random.choice([-1, 1])))

   # add label
   label = mySprites.Label("Hello, World!", (320, 240), "Comic Sans", random.randint(5, 30), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
   

   # add circle
   circle = mySprites.Circle((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

   # Add list of 10 Brick Sprites to one OrderedUpdates Sprite Group
   allSprites = pygame.sprite.OrderedUpdates(bricks, label, circle)
   
   # Assign 
   keepGoing = True
   clock = pygame.time.Clock()
   
   # Loop
   while keepGoing:
    
      # Time
      clock.tick(30)
    
      # Events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keepGoing = False
        
      # Refresh screen
      allSprites.clear(screen, background)
      allSprites.update()
      allSprites.draw(screen)  
      pygame.display.flip()

   # Close the game window
   pygame.quit()     
      
# Call the main function
main()    