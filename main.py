import pygame
from pygame.draw import *
from random import randint
import math

FPS = 10
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCORE = 0


def main():
    global balls_x, balls_y, balls_vx, balls_vy
    pygame.init()
    # get screen handler
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # pygame.display.update() #??????
    # set update time
    clock = pygame.time.Clock()
    finished = False
    new_ball(screen)
    pygame.display.update()
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
        pygame.display.update()
        screen.fill(BLACK)
        draw_ball(screen)
        wall_detection()
        #move ball
        balls_x += balls_vx
        balls_y += balls_vy

    print(SCORE)
    pygame.quit()


def new_ball(screen):
    '''рисует новый шарик '''
    global balls_vx, balls_vy, balls_x, balls_y, balls_r, balls_color  # make x,y,r global
    balls_x = randint(100, SCREEN_WIDTH - 100)
    balls_y = randint(100, SCREEN_HEIGHT)
    balls_r = randint(10, 100)
    balls_vx = randint(-20, 20)
    balls_vy = randint(-20, 20)

    balls_color = COLORS[randint(0, 5)]
    circle(screen, balls_color, (balls_x, balls_y), balls_r)


def wall_detection():
    global balls_x, balls_y, balls_vx, balls_vy
    new_x = balls_x + balls_vx
    new_y = balls_y + balls_vy
    if new_x + balls_r > SCREEN_WIDTH or new_x - balls_r < 0:
        balls_vx = -balls_vx
    if new_y - balls_r < 0 or new_y + balls_r > SCREEN_HEIGHT:
        balls_vy = -balls_vy


def draw_ball(screen):
    circle(screen, balls_color, (balls_x, balls_y), balls_r)
    pygame.display.update()


def click(event):
    global SCORE
    click_x, click_y = event.pos
    # pifagor teorem # check if clicked on object
    if math.sqrt(math.pow(math.fabs(click_x - balls_x), 2) + math.pow(math.fabs(click_y - balls_y), 2)) < balls_r:
        print('hit')
        SCORE += 1
    else:
        print('nope')


if __name__ == "__main__":
    main()
