import pygame
import random
def displayText(text, screen, position=(200,200), rect_size=200):
    myfont = pygame.font.Font(None, 36)
    text_rendering = myfont.render(text, True, (255,255,255))
    screen.blit(text_rendering, position, pygame.Rect(0,0,rect_size,rect_size))


class Snake:
    score = 0
    speed = 0
    size = 0
    color = ""
    blocks = [[]]

    def draw(self, screen):
        for block in self.blocks:
            pygame.draw.rect(screen, self.color, pygame.Rect(*block, self.size, self.size))
    
    def move(self, keys, movement=True):
        head = list(self.blocks[0])
        if movement:
            if keys[pygame.K_UP]:
                head[1] -= self.speed
            elif keys[pygame.K_DOWN]:
                head[1] += self.speed
            elif keys[pygame.K_RIGHT]:
                head[0] += self.speed
            elif keys[pygame.K_LEFT]:
                head[0] -= self.speed

        
            self.blocks.insert(0, head)
    
    def gameover(self, screen_dim, window):
        head = list(self.blocks[0])

        if head[0] < 0 or head[1]<0 or head[0]> screen_dim[0] or head[1]>screen_dim[1]:
            displayText("Game Over", window)
            displayText("Press T To Try Again", window, (200, 250), 300)
            displayText("Press Q To Quit", window, (200, 300))
            return True
        return False

    def ate(self, food_coord, movement):
    
        head = self.blocks[0]
        if movement:
            if abs(head[0] - food_coord[0]) <= 10 and abs(head[1] - food_coord[1]) <= 10:
                self.score += 1
                return True
            else:
                self.blocks.pop()
                return False
        


class Food:
    color = ""
    size = 0
    x, y = 0, 0
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


pygame.init()
width, height =800, 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

running = True

player = Snake()
player.blocks = [[100, 100]]
player.size = 20
player.speed = 10
player.color = "green"
food=Food()
food.color="red"
food.size=10
food.x=random.randint(0,width-10)
food.y=random.randint(0,height-10)
movement=True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        

    
    screen.fill("black")
    player.draw(screen)
    player.move(keys, movement=movement)
    food.draw(screen)
    gameover = player.gameover([width, height], screen)
    if gameover:
        movement=False
        if keys[pygame.K_t]:
            movement=True
            player.blocks = [[100, 100]]
            player.size = 20
            player.speed = 20
            player.color = "green"
        elif keys[pygame.K_q]:
            running=False
    if player.ate([food.x, food.y], movement):
        food.x=random.randint(0,width-10)
        food.y=random.randint(0,height-10)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()