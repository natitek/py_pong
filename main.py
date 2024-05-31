import pygame

# Example file showing a basic pygame "game loop"
import pygame

screen_width = 720
screen_height = 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    

    # RENDER YOUR GAME HERE
    

  
    pygame.draw.rect(screen,'white',player_rec,0)
    pygame.draw.line(screen,'white',(0,screen_height-50),(screen_width,screen_height-50))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        print("this")
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
