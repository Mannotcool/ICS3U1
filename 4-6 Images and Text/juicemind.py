"""
    Author: Nick
    
    Date: November 25th, 2024
    
    Description: Animating 3 images with a System and Custom Font.
"""

"""
    YOUR TASKS:
    
    1. Instead of animating 3 shapes, load and animate 3 images 
       (perhaps your favourite video game characters).

    2. Demonstrate how to use a System font and a Custom font to 
       put some text on the screen.  I have provided a custom font 
       called Gringo Nights but feel free to find and upload your own.

"""

import pygame

def main():
    '''This function defines the 'mainline logic' for our game.'''
    # I - INITIALIZE
    pygame.init()

    # DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Crazy Shapes Animation")

    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0)) 

    # Load 3 images using red_box, green_rect, and blue_circle
    red_box = pygame.image.load("Cherry.png")
    red_box = red_box.convert()

    green_rect = pygame.image.load("Ghost.png")
    green_rect = green_rect.convert()

    blue_circle = pygame.image.load("PacMan.png")
    blue_circle = blue_circle.convert()

    # A - ACTION (broken into ALTER steps)

    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    red_box_x = 0      # Assign starting (x,y)
    red_box_y = 200    # for our red box
    red_box_xdir = 5   # start moving left->right

    green_rect_x = 200     # Assign starting (x,y)
    green_rect_y = 0       # for our green rectangle
    green_rect_ydir = 7    # start moving top->bottom

    blue_circle_x = 400     # Assign starting (x,y)
    blue_circle_y = 400     # for our blue circle
    blue_circle_xdir = 7    # start moving left->bottom
    blue_circle_ydir = 9    # start moving top->bottom

    # Put some text on the screen that says pacman and uses custom font
    myCustomFont = pygame.font.Font("GringoNights.ttf", 60)
    label1 = myCustomFont.render("Pacman", True, (255, 255, 0))

    # LOOP
    while keepGoing:

        # TIMER
        clock.tick(30)

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # change x coordinate of red box
        red_box_x += red_box_xdir
        # check boundaries, to reset its direction
        if red_box_x+25 > screen.get_width() or red_box_x < 0:
            red_box_xdir = -red_box_xdir

        # change y coordinate of green rectangle
        green_rect_y += green_rect_ydir
        # check boundaries, to reset its direction
        if green_rect_y+25 > screen.get_height() or green_rect_y < 0:
            green_rect_ydir = -green_rect_ydir


        # change x & y coordinates of blue circle
        blue_circle_x += blue_circle_xdir
        blue_circle_y += blue_circle_ydir
        # check boundaries, to reset its direction
        if blue_circle_x+24 > screen.get_width() or blue_circle_x < 0:
            blue_circle_xdir = -blue_circle_xdir
        if blue_circle_y+24 > screen.get_height() or blue_circle_y < 0:
            blue_circle_ydir = -blue_circle_ydir


        # REFRESH (update window)
        screen.blit(background, (0, 0))
        screen.blit(red_box, (red_box_x, red_box_y))               # blit box at new (x,y) location
        screen.blit(green_rect, (green_rect_x, green_rect_y))      # blit rectangle at new (x,y) location
        screen.blit(blue_circle, (blue_circle_x, blue_circle_y))   # blit circle at new (x,y) location
        screen.blit(label1, (220, 40))
        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()