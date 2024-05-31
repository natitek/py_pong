
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
ball_x=100
ball_y=screen_height/2
player1_score=0
player2_score=0
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def colision():
    global right
    global left
    global down
    global up
    global ball_x
    global ball_y
    global player1_score
    global player2_score
    Key=pygame.key.get_pressed()
    
    
    if (ball_x-15) <= (player1_x+20) :
        for x in range(int(player1_y),int(player1_y+150)):
            if ball_y==x :
                x=player1_y+151
                left=False
                right=True
                print("right")
                if Key[pygame.K_w]:
                    up=True
                    down=False
                    print("up")
                elif Key[pygame.K_s]:
                    up=False
                    down=True
                
            print("bo")
            
    elif ball_x+15 >= player2_x :
            for x in range(int(player2_y),int(player2_y+150)):
                if ball_y==x :
                    x=player2_y+151
                    left=True
                    right=False
                    if Key[pygame.K_i]:
                        up=True
                        down=False
                    elif Key[pygame.K_k]:
                        up=False
                        down=True
                    break
                print("bo2")
    if(ball_y<=0):
        up=False
        down=True
    elif(ball_y>=600):
        down=False
        up=True
    if(ball_x<=0):
        ball_x=screen_width/2
        ball_y=screen_height/2
        left=True
        right=False
        player2_score+=1
    elif(ball_x>=1000):
        ball_x=screen_width/2
        ball_y=screen_height/2
        right=True
        left=False
        player1_score+=1
    if left:
        ball_x -= 3
    if right:
        ball_x += 3
    if down:
        ball_y += 3
    if up:
        ball_y -= 3

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
    colision()

    if keys[pygame.K_w]:
        player1_y -= 10
    elif keys[pygame.K_s]:
        player1_y += 10
    if keys[pygame.K_i]:
        player2_y -= 10
    elif keys[pygame.K_k]:
        player2_y += 10

    if (player1_y) > 600-150:
        player1_y = 600-150
    if (player1_y) < 0:
        player1_y = 0
    if (player2_y) > 600-150:
        player2_y = 600-150
    if (player2_y) < 0:
        player2_y = 0

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
