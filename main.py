
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
choice=input("1,singleplayer 2,multiplayer \n")
if(int(choice)==1):
    multi=False
else:
    multi=True
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
#ai movment
def ai():
    global player1_y
    global player1_x
    global player2_y
    global player2_x
    global ball_x
    global ball_y
    global right
    global left
    global multi

    #makes the pad proportional to the balls y position
    if(ball_x>=(screen_width/2)and not(multi) and right):
        if(ball_y>(player2_y+75)):
            player2_y+=5
        elif(ball_y<(player2_y+75)):
            player2_y-=5
        
#returns the pad to the center
    elif(not(multi) and left):
        if((player2_y+75)>(screen_height/2)):
            player2_y-=5
        elif((player2_y+75)<(screen_height/2)):
            player2_y+=5
def colision():
    global right
    global left
    global down
    global up
    global ball_x
    global ball_y
    global player1_y
    global player1_x
    global player2_y
    global player2_x
    global ball_y
    global player1_score
    global player2_score
    global multi
    Key=pygame.key.get_pressed()
    
    #userone ball contact
    if (ball_x-15) <= (player1_x+20) :
        for x in range(int(player1_y),int(player1_y+150)):
            if ball_y==x :
                x=player1_y+151
                left=False
                right=True
                if Key[pygame.K_w]:
                    up=True
                    down=False
                elif Key[pygame.K_s]:
                    up=False
                    down=True
                
          #playertwo ball contact  
    elif ball_x+15 >= player2_x:
            for x in range(int(player2_y),int(player2_y+150)):
                if ball_y==x :
                    x=player2_y+151
                    left=True
                    right=False
                    if Key[pygame.K_i]and multi:
                        up=True
                        down=False
                    elif Key[pygame.K_k] and multi:
                        up=False
                        down=True
                    #ai logic
                    if ball_y<(player2_y+75)and not(multi):
                        up=True
                        down=False
                    elif ball_y>(player2_y+75) and not(multi):
                        up=False
                        down=True

                        #frame contact
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
        up=False
        down=False
        player2_score+=1
    elif(ball_x>=1000):
        ball_x=screen_width/2
        ball_y=screen_height/2
        right=True
        left=False
        up=False
        down=False
        player1_score+=1
        #ball movment
    if left:
        ball_x -= 5
    if right:
        ball_x += 5
    if down:
        ball_y += 5
    if up:
        ball_y -= 5

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
    ai()

    if keys[pygame.K_w]:
        player1_y -= 5
    elif keys[pygame.K_s]:
        player1_y += 5
    if keys[pygame.K_i] and multi:
        player2_y -= 5
    elif keys[pygame.K_k] and multi:
        player2_y += 5

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
