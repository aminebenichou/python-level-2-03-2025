# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
x = 0
y = 0
x_food = 100
y_food = 100
speed = 5
while running:
    # move snake
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_LEFT]:
        x -= speed
    # poll for events
    if (x>=x_food-5 and x<=x_food+5) and (y>=y_food-5 and y<=y_food+5):
        x_food= random.randint(10, 1250)
        y_food= random.randint(10, 720)
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    pygame.draw.rect(screen,'blue',(x,y,50,50)) #Snake
    pygame.draw.circle(screen, 'red', (x_food, y_food), 20) #Food
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()