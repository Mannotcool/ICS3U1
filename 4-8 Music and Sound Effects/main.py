"""
    Author: Nick S
    
    Date: Dec 2nd 2024
    
    Description: Animating 3 images with a System and Custom Font.
"""

"""
    YOUR TASKS:
    
    1. Add some background music (.ogg or .mp3 file).
       
    2. Add 3 different sound effects (.ogg or .wav file), one for 
       each image in your game.  Play a sound effect when each image
       changes direction in your animation.
"""

import pygame

def main():
    '''This function defines the 'mainline logic' for our game.'''
    # I - INITIALIZE
    pygame.init()
    pygame.mixer.init()


    # MUSIC
    pygame.mixer.music.load("music.ogg")
    pygame.mixer.music.set_volume(0.2) 
    pygame.mixer.music.play(-1)    # play forever

    # SOUND EFFECTS
    cherry_sound = pygame.mixer.Sound("cherry.wav")
    ghost_sound = pygame.mixer.Sound("ghost.wav")
    pacman_sound = pygame.mixer.Sound("pacman.wav")




    # DISPLAY
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Crazy Shapes Animation")

    # ENTITIES
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))    # white background

    cherry = pygame.image.load("Cherry.png")
    cherry.set_colorkey((0,0,0))    # Make any black pixels transparent
    
    ghost = pygame.image.load("Ghost.png")
    ghost.set_colorkey((0,0,0))    # Make any black pixels transparent

    pacman = pygame.image.load("PacMan.png")
    pacman.set_colorkey((0,0,0))    # Make any black pixels transparent

    # A - ACTION (broken into ALTER steps)

    # ASSIGN
    clock = pygame.time.Clock()
    keepGoing = True

    cherry_x = 0      # Assign starting (x,y)
    cherry_y = 200    # for our cherry
    cherry_xdir = 5   # start moving left->right

    ghost_x = 200     # Assign starting (x,y)
    ghost_y = 0       # for our ghost rectangle
    ghost_ydir = 7    # start moving top->bottom

    pacman_x = 400     # Assign starting (x,y)
    pacman_y = 400     # for our blue circle
    pacman_xdir = 7    # start moving left->bottom
    pacman_ydir = 9    # start moving top->bottom

    # LOOP
    while keepGoing:

        # TIMER
        clock.tick(30)

        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

        # change x coordinate of cherry
        cherry_x += cherry_xdir
        # check boundaries, to reset its direction
        if cherry_x+25 > screen.get_width() or cherry_x < 0:
            cherry_xdir = -cherry_xdir
            # play sound effect
            cherry_sound.play()



        # change y coordinate of ghost
        ghost_y += ghost_ydir
        # check boundaries, to reset its direction
        if ghost_y+25 > screen.get_height() or ghost_y < 0:
            ghost_ydir = -ghost_ydir
            # play sound effect
            ghost_sound.play()



        # change x & y coordinates of pacman
        pacman_x += pacman_xdir
        pacman_y += pacman_ydir
        # check boundaries, to reset its direction
        if pacman_x+24 > screen.get_width() or pacman_x < 0:
            pacman_xdir = -pacman_xdir
            # play sound effect
            pacman_sound.play()
        if pacman_y+24 > screen.get_height() or pacman_y < 0:
            pacman_ydir = -pacman_ydir
            # play sound effect
            pacman_sound.play()



        # REFRESH (update window)
        screen.blit(background, (0, 0))
        screen.blit(cherry, (cherry_x, cherry_y))               # blit box at new (x,y) location
        screen.blit(ghost, (ghost_x, ghost_y))      # blit rectangle at new (x,y) location
        screen.blit(pacman, (pacman_x, pacman_y))   # blit circle at new (x,y) location
        pygame.display.flip()

    # Close the game window
    pygame.quit()

# Call the main function
main()