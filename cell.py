import pygame


class cell:
    def __init__(self, left, top, width, height):
        self.rect = pygame.rect(left, top, width, height)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)
