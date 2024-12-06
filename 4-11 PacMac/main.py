"""
    Author: < Your Name Here >
    
    Date: May 11, 2022
    
    Description: Simple PacMan Game
"""

"""
    YOUR TASKS:
    
    1. Create a "Cherry" Sprite subclass in the mySprites.py module
       to represent cherry sprites in this game.  Model your class 
       after the Brick class we have discussed.  When a Cherry sprite 
       is instantiated it should appear at a random position in the 
       game window.
       
    2. In main() create a cherriesGroup OrderedUpdates group containing
       10 Cherry sprites.
       
    3. Complete the goDown(), goLeft(), goRight(), and update() methods
       in the PacMan class. In the update() method, if PacMan goes past
       the edge of the window he should reappear on the opposite side
       of the window travelling in the same direction.
       
    4. Complete Event handling so that PacMan can go left, up, and down too.
    
    5. Add Collision detection between pacman and cherriesGroup.  Add 1 point
       for each cherry collision, and kill() the cherry.
       
    6. Play a sound effect for each point scored.
"""

import pygame
import mySprites
           
def main():
    '''This function defines the 'mainline logic' for our game.'''
    # Initialize pygame
    pygame.init()
     
    # Display
    screen = pygame.display.set_mode((640, 480))    
    pygame.display.set_caption("Using the mySprites library")
    
    # Entities
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    # Create ScoreKeeper and Pacman sprites
    score = mySprites.ScoreKeeper()
    pacman = mySprites.PacMan(screen)

    # 2. CREATE LIST OF 10 "Cherry" SPRITES, ADD THEM TO "cherriesGroup"
    cherries = []
    for _ in range(10):
        cherries.append(mySprites.Cherry(screen))
        
    cherriesGroup = pygame.sprite.OrderedUpdates(cherries)
    allSprites = pygame.sprite.OrderedUpdates(cherries, pacman, score)
    
    # ACTION

    # load pacman.wav sound effect
    pacman_sound = pygame.mixer.Sound("pacman.wav")
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pacman.goRight()
                # 4. ADD EVENTS FOR LEFT, UP, AND DOWN
                if event.key == pygame.K_LEFT:
                    pacman.goLeft()
                if event.key == pygame.K_UP:
                    pacman.goUp()
                if event.key == pygame.K_DOWN:
                    pacman.goDown()
                    
        # 5. ADD COLLISION DETECTION TO ADD 1 POINT FOR EACH CHERRY HIT
        if pygame.sprite.spritecollide(pacman, cherriesGroup, True):
            score.addPoint()
            pacman_sound.play()
            
        # GAME OVER if 10 points have been scored
        if score.getPoints() == 10:
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
