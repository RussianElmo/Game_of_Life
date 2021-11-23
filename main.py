import sys
import pygame

from cell import cell
from alive import alive
from dead import dead


pygame.init()

size = width, height = 1000, 1000
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
blockList = []


def draw_grid():
    blockSize = 20
    for y in range(1000):
        for x in range(1000):
            c = dead(x * (blockSize + 1), y * (blockSize + 1), blockSize, blockSize)
            c.draw(screen, white)
            blockList.append(c)


def change_state():
    clicked = 0
    for i in range(len(blockList)):
        if blockList[i].check_click(pygame.mouse.get_pos()):
            clicked = blockList[i]
            index = i
            break
    if isinstance(clicked, dead):
        dead_rect = clicked.rect
        blockList[index] = alive(dead_rect.left, dead_rect.top, dead_rect.width, dead_rect.height)
        blockList[index].draw(screen, black)
        pygame.display.flip()
    elif isinstance(clicked, alive):
        alive_rect = clicked.rect
        blockList[index] = dead(alive_rect.left, alive_rect.top, alive_rect.width, alive_rect.height)
        blockList[index].draw(screen, white)
        pygame.display.flip()



screen.fill(black)
draw_grid()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            change_state()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            print(1)
            for block in blockList:
                print(block.stay(blockList))
