import pygame
from pygame.draw import *
from random import randint
import math

FPS = 2
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


def main():
    pygame.init()
    #get screen handler
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #pygame.display.update() #??????
    #set update time
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click(event)
        new_ball(screen)
        pygame.display.update()
        screen.fill(BLACK)

    pygame.quit()


def new_ball(screen):
    '''рисует новый шарик '''
    global balls_x, balls_y, balls_r  # make x,y,r global
    balls_x = randint(100, SCREEN_WIDTH-100)
    balls_y = randint(100, SCREEN_HEIGHT)
    balls_r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (balls_x, balls_y), balls_r)


def click(event):
    click_x, click_y = event.pos
    # pifagor teorem # check if clicked on object
    if math.sqrt(math.pow(math.fabs(click_x - balls_x), 2) + math.pow(math.fabs(click_y - balls_y), 2)) < balls_r:
        print('hit')
    else:
        print('nope')


if __name__ == "__main__":
    main()
