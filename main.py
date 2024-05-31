
# Example file showing a basic pygame "game loop"
import pygame

screen_width = 1000
screen_height = 600
left=True
right=False
down=False
up=False
player1_x = 0
player2_x = screen_width -20
player1_y = screen_height/2
player2_y = screen_height/2
ball_x=screen_width/2
ball_y=screen_height/2
player1_score=0
player2_score=0
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def colision(ballx,bally, recx:int,recy:int):
    global right
    global left
    global down
    global up
    global ball_x
    global ball_y
    global player1_score
    global player2_score
    Key=pygame.key.get_pressed()
    for x in range(recy,recy+150):
        if bally==x :
            if ballx-15 <= recx+20 and left :
                left=False
                right=True
                if Key[pygame.K_w]:
                    up=True
                    down=False
                elif Key[pygame.K_s]:
                    up=False
                    down=True
            elif ballx+15 >= recx and right :
                left=True
                right=False
                if Key[pygame.K_w]:
                    up=True
                    down=False
                elif Key[pygame.K_s]:
                    up=False
                    down=True
    if(bally<=0):
        up=False
        down=True
    elif(bally>=600):
        down=False
        up=True
    if(ballx<=0):
        ball_x=screen_width/2
        ball_y=screen_height/2
        left=True
        right=False
        player2_score+=1
    elif(ballx>=1000):
        ball_x=screen_width/2
        ball_y=screen_height/2
        right=True
        left=False
        player1_score+=1

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

    colision(ball_x,ball_y,int(player1_x),int(player1_y))
    colision(ball_x,ball_y,int(player2_x),int(player2_y))


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

    if left:
        ball_x -= 3
    if right:
        ball_x += 3
    if down:
        ball_y += 3
    if up:
        ball_x -= 3
    


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
