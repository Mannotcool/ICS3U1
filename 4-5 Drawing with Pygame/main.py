# N.S 4-5

# I - Import and Initialize
import pygame, math
pygame.init()
 
def drawStuff(background):
    # the head
    pygame.draw.rect(background, (0, 255, 0), ((50, 50), (50, 50)), 0)
    # the eyes
    pygame.draw.rect(background, (0, 0, 0), ((60, 60), (10, 10)), 0)
    pygame.draw.rect(background, (0, 0, 0), ((80, 60), (10, 10)), 0)

    # the mouth
    pygame.draw.rect(background, (0, 0, 0), ((70, 70), (10, 10)), 0)
    pygame.draw.rect(background, (0, 0, 0), ((60, 80), (30, 10)), 0)
    pygame.draw.rect(background, (0, 0, 0), ((60, 90), (10, 10)), 0)
    pygame.draw.rect(background, (0, 0, 0), ((80, 90), (10, 10)), 0)

    # the body
    pygame.draw.rect(background, (0, 255, 0), ((50, 100), (50, 90)), 0)

    # the legs
    pygame.draw.rect(background, (0, 255, 0), ((50, 190), (20, 10)), 0)
    pygame.draw.rect(background, (0, 255, 0), ((80, 190), (20, 10)), 0)

    # black lines at the bottom of the feet
    pygame.draw.line(background, (0, 0, 0), (50, 200), (70, 200), 1)
    pygame.draw.line(background, (0, 0, 0), (80, 200), (100, 200), 1)
     
def main():
    # D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Drawing commands")
 
    # E - Entities (just background for now)    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
     
    drawStuff(background)
     
    # A - Action (broken into ALTER steps)
     
    # A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
     
    # L - Loop
    while keepGoing:
        # T - Timer to set frame rate
        clock.tick(30)
         
        # E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())    
         
        # R - Refresh display
        screen.blit(background, (0, 0))
        pygame.display.flip()
     
    # Close the game window
    pygame.quit()    
 
# Call the main function
main()