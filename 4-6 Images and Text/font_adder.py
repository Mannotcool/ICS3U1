# N.S 4-6

# I - Import and Initialize
import pygame
pygame.init()
     
def main():
    # D - Display configuration
    screen = pygame.display.set_mode((320, 480))
    pygame.display.set_caption("display some text")
    
    # E - Entities (just background for now)    
    background = pygame.Surface((640, 480))
    background.fill((255, 255, 255))
    
    creeper = pygame.image.load("myImage.png")
    creeper = creeper.convert()
     
    mySystemFont = pygame.font.SysFont("Comic Sans", 60)
    label1 = mySystemFont.render("creeper", True, (0, 255, 0))
     
    screen.blit(background, (0, 0))
    screen.blit(creeper, (80, 20))
    screen.blit(label1, (50, 200))
        
    pygame.display.flip()
    pygame.image.save(screen, "newImage.bmp")
    # Close the game window
    pygame.quit()    
 
# Call the main function
main()