import pygame

# Example file showing a basic pygame "game loop"
import pygame

screen_width = 1000
screen_height = 600
left=True
right=False
down=False
up=False
ball_x=screen_width/2
ball_y=screen_height/2
player1_score=0
player2_score=0
# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

def colision(ballx,bally,recx,recy):
    global right
    global left
    global down
    global up
    global ball_x
    global ball_y
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

    

    # RENDER YOUR GAME HERE

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        print("this")
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
