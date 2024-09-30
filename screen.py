import random

from consts import *
import pygame as pg

BLACK = (0, 0, 0)
green = (0, 180, 0)



def main():
    global SCREEN, CLOCK
    pg.init()
    SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pg.time.Clock()
    SCREEN.fill(BLACK)

    drawGrid()
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()


        pg.display.update()


def drawGrid():
    blockSize = 30 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pg.Rect(x, y, blockSize, blockSize)
            pg.draw.rect(SCREEN, green, rect, 1)
    list_a = []
    list_b = []
    for i in range(0, 1470, 30):
        list_a.append(i)
    for i in range(0, 720, 30):
        list_b.append(i)
    mine = pg.image.load(MINE_IMAGE).convert()
    mine.set_colorkey((0, 0, 0))
    for i in range(20):
        a = random.choice(list_a)
        b = random.choice(list_b)
        SCREEN.blit(mine, [a, b])
        pg.display.flip()
    shimi_danger = pg.image.load(SOLDIER_DANGER_IMAGE).convert()
    shimi_danger = pg.transform.scale(shimi_danger, (60, 90))
    shimi_danger.set_colorkey((0, 0, 0))

    SCREEN.blit(shimi_danger, [0, 0])
    pg.display.flip()


main()
