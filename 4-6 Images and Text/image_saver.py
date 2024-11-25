# N.S 4-6

# I - Import and Initialize
import pygame
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
    # E - Entities (just background for now)    
    background = pygame.Surface((640, 480))
    background.fill((255, 255, 255))
    
    drawStuff(background)
     
    # A - Action (broken into ALTER steps)
    pygame.image.save(background, "creeper.png")
     
    # Close the game window
    pygame.quit()    
 
# Call the main function
main()