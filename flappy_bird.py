import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Flappy Bird')
# Function to display text
def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont('freesansbold', 32)
    msgobj = fontobj.render(msg, True, color)
    screen.blit(msgobj, (x, y))
# Game function
def play_flappybird():
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    birdx, birdy = 300, 300
    pipe_x = 600
    score = 0
    velocity = 0
    height = random.randint(50, 250)
    running = True
    clock=pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        # Show score
        show_text('Score: ' + str(score), 450, 0, blue)
        # Bird movement (gravity + jump)
        velocity += 0.1
        birdy += velocity
        bird = pygame.draw.circle(screen, yellow, (birdx, int(birdy)), 20)
        # Pipes
        top_pipe = pygame.draw.rect(screen, green, (pipe_x, 0, 50, height))
        bottom_y = height + 150
        bottom_pipe = pygame.draw.rect(screen, green, (pipe_x, bottom_y, 50, 600 - bottom_y))
        # Move pipes
        pipe_x -= 2
        if pipe_x < -50:
            pipe_x = 600
            height = random.randint(50, 250)
            score += 1
        # Collision detection
        if (bird.colliderect(top_pipe) or bird.colliderect(bottom_pipe) or birdy > 600 or birdy < 0):
            screen.fill((0, 0, 0))
            show_text('Game Over', 200, 250, red)
            pygame.display.update()
            time.sleep(2)
            running = False
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    velocity = -3
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        clock.tick(20)
        pygame.display.update()
#Main Menu Loop
while True:
    red=(255,0,0)
    blue=(0,0,255)
    screen.fill((0,0,0))
    pygame.draw.rect(screen, red, (50,250,200,100))
    pygame.draw.rect(screen, red, (350,250,200,100))
    show_text('Play', 120,285,blue)
    show_text('Quit', 420,285,blue)
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 50<event.pos[0] and 250<event.pos[1]<350:
                print('play')
                screen.fill((0,0,0))
                play_flappybird()
            if 350<event.pos[0]<550 and 250<event.pos[1]<350:
                pygame.quit()
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    
