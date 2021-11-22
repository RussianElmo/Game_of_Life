import sys

import pygame

pygame.init()

size = width, height = 320, 240
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
blockList = []


def draw_grid():
    blockSize = 20
    for x in range(0, size[0], blockSize):
        for y in range(0, size[1], blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            blockList.append(rect)
            pygame.draw.rect(screen, black, rect, 1)


screen.fill(white)
draw_grid()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.get_pos()
