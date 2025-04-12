# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720)) # Fenetre
clock = pygame.time.Clock()
running = True
x = 0
y = 0
snake = [[50,50]]
snake_size = 25
food_size = 20
trigger = food_size+(snake_size/2)
x_food = 100
y_food = 100
speed = 10
score = 0
gameover= False

def displayText(text, position=(200,200), rect_size=200):
    myfont = pygame.font.Font(None, 36)
    text_rendering = myfont.render(text, True, (255,255,255))
    screen.blit(text_rendering, position, pygame.Rect(0,0,rect_size,rect_size))

def gameOver():
    displayText("Game Over", (200,200), 200)
    displayText("Try Again => Press Enter", (200,250), 200)
    displayText("Press Any To Quit", (200,300), 200)
    return True

while running:
    # move snake
    myfont = pygame.font.Font(None, 36)
    score_text = myfont.render("Score: " + str(score), True, (255, 255, 255))
    keys = pygame.key.get_pressed()
    if not gameover:
        head = list(snake[0])
        if keys[pygame.K_UP]:
            head[1] -= speed
        elif keys[pygame.K_DOWN]:
            head[1] += speed
        elif keys[pygame.K_RIGHT]:
            head[0] += speed
        elif keys[pygame.K_LEFT]:
            head[0] -= speed
        
        snake.insert(0, head)

        # poll for events
        if (snake[0][0]>=x_food-trigger and snake[0][0]<=x_food+trigger) and (snake[0][1]>=y_food-trigger and snake[0][1]<=y_food+trigger):
            x_food= random.randint(10, 1250)
            y_food= random.randint(10, 720)
            score += 10
            print(snake)
        else:
            snake.pop()


    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if gameover:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    x=0
                    y=0
                    gameover=False
                    score=0
                    x_food=100
                    y_food=100
                else:
                    running=False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if head[0]<0 or head[1]<0 or head[0]>1280 or head[1]>720:
        gameover = gameOver()
    # RENDER YOUR GAME HERE
    for block in snake:
        pygame.draw.rect(screen,'blue',(*block,snake_size,snake_size)) #Snake
    
    
    pygame.draw.circle(screen, 'red', (x_food, y_food), food_size) #Food

    # flip() the display to put your work on screen
    displayText(f"Score: {score}", (10,10), 200)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()