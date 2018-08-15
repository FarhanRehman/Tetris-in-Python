import pygame

class Block():
    def __init__(self, color, gridx, gridy):
        self.color = color
        self.gridx = int(gridx)
        self.gridy = int(gridy)
        self.size = 25

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.gridx * self.size, self.gridy * self.size, self.size - 1, self.size - 1], 0)
