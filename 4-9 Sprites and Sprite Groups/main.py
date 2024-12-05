"""
    Author: Nick S
    
    Date: Dec 3rd, 2024
    
    Description: Demonstrating my Box sprite!
"""

"""
    YOUR TASKS:
    
    1. Modify the Box sprite initializer code so that each Box you 
       instantiate can have a unique x direction value.  The main() code 
       below has already been adjusted for this change; i.e., one Box will
       move right and the other left at slightly different speeds.
       
    2. Modify the Box sprite initializer to include a y direction, and change 
       its update() method so that boxes can travel diagonally and bounce off 
       the top and bottom of the window (just like your blue circle in 
       Repl 4-3 Crazy Shapes).  Update main() to demonstrate *2* Box sprites 
       moving in different x & y directions.  Can you make the x and y 
       directions random in main()?
       
    3. Modify the Box sprite initializer code so that each Box you
       instantiate can have a different RGB color.  Add 3 additional integer
       parameters to the Box sprite initializer to accept individual R, G, 
       and B values.  Update main() to demonstrate *3* Box sprites with random
       RGB colours moving random directions.  
       
    4. Update main() to demonstrate *10* boxes, each with
       a random RGB colour, and moving in random x and y directions.  
       Hint: Use a *loop* to create a *list* of Box sprite objects, then pass the
       list of Box sprites into OrderedUpdates().
       
    5. Do *NOT* add music or sound effects to your code, or it will not run in Coding Rooms.
"""

# Import and Initialize
import pygame
import mySprites
import random
pygame.init()


def main():
    '''This function defines the 'mainline logic' for our game.'''
    
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Sprite Demo")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 0))
    screen.blit(background, (0,0))
    
    # Create ten Box sprites with random RGB colours and random directions, and random x and ys use random module. Use loop to create list of Box sprite objects.
    boxList = []
    for _ in range(10):
        x = random.randint(0, 620)
        y = random.randint(0, 460)
        xdir = random.randint(-5, 5)
        ydir = random.randint(-5, 5)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        box = mySprites.Box(screen, x, y, xdir, ydir, r, g, b)
        boxList.append(box)
    
    # Add our Box sprites to an OrderedUpdates Sprite Group to keep Refresh section simple
    allSprites = pygame.sprite.OrderedUpdates(boxList)
    
    # ACTION
    
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
    
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
        # The next line automatically calls the update() method 
        # for any sprites in the allSprites group.
        allSprites.update()
        allSprites.draw(screen)
    
        pygame.display.flip()

    # Close the game window
    pygame.quit()        

# Call the main function
main()
