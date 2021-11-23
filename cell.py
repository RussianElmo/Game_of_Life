import pygame


class cell:
    def __init__(self, left, top, width, height):
        self.rect = pygame.Rect(left, top, width, height)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rect)

    def get_rect(self):
        return self.rect

    def check_click(self, pos):
        return self.rect.collidepoint(pos)