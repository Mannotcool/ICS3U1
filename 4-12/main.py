# Tag Game, where there are 2 boxes and 2 controllers. The boxes can be moved by the controllers. If the boxes collide, the box that was hit will change color.
# if they collide, kill the game

# I - Import and Initialize
import pygame, mySprites
pygame.init()
     
def main():
    pygame.joystick.init()
    '''This function defines the 'mainline logic' for our game.'''
      
    # Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move the rectangle with the joystick!")
     
    # Entities
    # Create a list of Joystick objects.
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)    
 
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))
     
    # Create a Box sprite object
    box_p1 = mySprites.Box(screen, 200)
    box_p2 = mySprites.Box(screen, 400)

    allSprites = pygame.sprite.OrderedUpdates(box_p1, box_p2)
 
    # ACTION
     
    # Assign 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # Loop
    while keepGoing:
     
        # Time
        clock.tick(30)
     
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            
            # 3. Add code to handle joystick events
            if event.type == pygame.JOYBUTTONDOWN:
                if event.joy == 0:
                    box_p1.changeColour(event.button)
                elif event.joy == 1:
                    box_p2.changeColour(event.button)
            elif event.type == pygame.JOYAXISMOTION:
                if event.joy == 0:
                    box_p1.changeDirection((joysticks[0].get_axis(0), joysticks[0].get_axis(1)))
                elif event.joy == 1:
                    box_p2.changeDirection((joysticks[1].get_axis(0), joysticks[1].get_axis(1)))
            
        # Check for collisions
        if pygame.sprite.collide_rect(box_p1, box_p2):
            box_p1.changeColour(0)
            box_p2.changeColour(0)
            box_p1.kill()
            box_p2.kill()
            keepGoing = False
         
        # Refresh screen
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
         
        pygame.display.flip()
         
    # Unhide mouse pointer
    pygame.mouse.set_visible(True)
 
    # Close the game window
    pygame.quit()    
     
# Call the main function
main()