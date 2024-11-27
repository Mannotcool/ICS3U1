"""
    Author: Nick S

    Date: November 27th 2024
    
    Description: A simple paint program using pygame!
"""

"""
    YOUR TASKS:
    
    1. Add events for the keys 'r', 'g', and 'b' such that they change 
       the current drawing colour to red, green, and blue respectively.

    2. Add events for the keys '1' through '9' such that they set the 
       line width to that many pixels.
       
    3. Add an event for the 's' (save) key that will cause the current 
       picture to be saved in the current directory with the filename: painting.png
       
    4. Add an event for the 'l' (load) key that will cause the painting.png 
       file to be loaded and displayed in the window.
"""

import pygame

def statusSurface(drawColor, lineWidth):
    """ creates a Surface object for status text """
    myFont = pygame.font.SysFont("Courier", 20)
    status_string = "color: " + str(drawColor) + ", width: " + str(lineWidth)
    status = myFont.render(status_string, 1, (drawColor))
    return status

def main():
    '''This function defines the 'mainline logic' for our paint program.'''
    # I - Initialize pygame
    pygame.init()
    
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint:  (w)hite, blac(k), (c)lear, (q)uit")
    
    # E - Entities
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    
    # A - Action (broken into ALTER steps)
    
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3
    
    # L - Loop
    while keepGoing:
   
        # T - Timer to set frame rate
        clock.tick(30)
    
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
		# Check if left mouse button is down
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    #quit    
                    keepGoing = False
                elif event.key == pygame.K_c:
                    #clear screen
                    background.fill((255, 255, 255))
                elif event.key == pygame.K_w:
                    #white
                    drawColor = (255, 255, 255)
                elif event.key == pygame.K_k:
                    #black
                    drawColor = (0, 0, 0)
            

        # R - Refresh display
        screen.blit(background, (0, 0))
        myLabel = statusSurface(drawColor, lineWidth)
        screen.blit(myLabel, (300, 450))
        pygame.display.flip()

    # Close the game window
    pygame.quit()   
       
# Call the main function
main()