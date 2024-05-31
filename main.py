import pygame

# Example file showing a basic pygame "game loop"
import pygame

screen_width = 1000
screen_height = 600
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

player1_y = screen_height/2
player2_y = screen_height/2

player1_score = 0
player2_score = 0

ball_x = screen_width/2
ball_y = screen_height/2

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    
    player1 = pygame.Rect(0,player1_y,20,150)
    player2 = pygame.Rect(screen_width-20,player2_y,20,150)

    # RENDER YOUR GAME HERE
   
    pygame.draw.rect(screen,'white',player1,0)
    pygame.draw.rect(screen,'white',player2,0)
    # pygame.draw.line(screen,'white',(0,screen_height-50),(screen_width,screen_height-50))
    pygame.draw.circle(screen,"red",(ball_x,ball_y),15)
    pygame.font.get_init()
    my_font = pygame.font.SysFont('Noto Sans Display', 50)

    text_surface = my_font.render(str(player1_score), False, (255,255,255))
    text_surface2 = my_font.render(str(player2_score), False, (255,255,255))


    screen.blit(text_surface, ((screen_width/2)-50,0))
    screen.blit(text_surface2, ((screen_width/2)+50,0))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player1_y -= 10
    if keys[pygame.K_s]:
        player1_y += 10
    if keys[pygame.K_i]:
        player2_y -= 10
    if keys[pygame.K_k]:
        player2_y += 10

    if (player1_y) > 600-150:
        player1_y = 600-150
    if (player1_y) < 0:
        player1_y = 0
    if (player2_y) > 600-150:
        player2_y = 600-150
    if (player2_y) < 0:
        player2_y = 0


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
