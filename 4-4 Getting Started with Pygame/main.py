"""
    Author: Nick S
    
    Date: Nov 20, 2024
    
    Description: Animating Shapes with pygame
"""

import pygame # type: ignore

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
    background.fill((255, 255, 255))    # white background

    # Make a red 25 x 25 box
    red_box = pygame.Surface((25, 25))
    red_box = red_box.convert()
    red_box.fill((255, 0, 0))

    # Make a green 40 x 20 rectangle
    green_rect = pygame.Surface((40, 20))
    green_rect = green_rect.convert()
    green_rect.fill((0, 255, 0))

    # Make a blue 24 x 24 circle
    blue_circle = pygame.Surface((24, 24))
    blue_circle = blue_circle.convert()
    blue_circle.fill((0, 0, 255))

    # A - ACTION (broken into ALTER steps)

    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    red_box_x = 0      # Assign starting (x,y)
    red_box_y = 200    # for our red box

    green_rect_x = 100
    green_rect_y = 0

    green_rect_dy = 3  # Change in y-direction

    # Blue circle initial properties
    blue_circle_x = 150
    blue_circle_y = 0

    blue_circle_dx = 3  # Change in x-direction
    blue_circle_dy = 3  # Change in y-direction

    # LOOP
    while keepGoing:

        # TIMER
        clock.tick(30)

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # change x coordinate of box
        red_box_x += 5

        # check boundaries, to reset box to left-side
        if red_box_x > screen.get_width():
            red_box_x = 0

        # Update green rectangle position
        green_rect_y += green_rect_dy

        # check boundaries, change direction and bounce back
        if green_rect_y <= 0 or green_rect_y >= screen.get_height() - 20:
            green_rect_dy = -green_rect_dy

        # Update blue circle position
        blue_circle_x += blue_circle_dx
        blue_circle_y += blue_circle_dy

        # Reverse direction if it hits the screen edges
        if blue_circle_x <= 0 or blue_circle_x >= screen.get_width() - 24:
            blue_circle_dx = -blue_circle_dx
        if blue_circle_y <= 0 or blue_circle_y >= screen.get_height() - 24:
            blue_circle_dy = -blue_circle_dy
     
        # REFRESH (update window)
        screen.blit(background, (0, 0))
        screen.blit(red_box, (red_box_x, red_box_y))   # blit box at new (x,y) location
        screen.blit(green_rect, (green_rect_x, green_rect_y))
        screen.blit(blue_circle, (blue_circle_x, blue_circle_y))
        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()