import pygame
import os
import math

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)

# Shapes
UNIT_LENGTH = 20

# I SHAPE
i_shape_points = [pygame.Vector2(200, 320), pygame.Vector2(200 + UNIT_LENGTH, 320),
    pygame.Vector2(200 + UNIT_LENGTH, 320 + 4 * UNIT_LENGTH),
    pygame.Vector2(200, 320 + 4 * UNIT_LENGTH)]
rotate_about_i = pygame.Vector2(200, 320 + 2 * UNIT_LENGTH)

# J SHAPE
j_shape_points = [pygame.Vector2(200, 320), pygame.Vector2(200 + UNIT_LENGTH, 320),
    pygame.Vector2(200 + UNIT_LENGTH, 320 - 2 * UNIT_LENGTH),
    pygame.Vector2(200 + 2 * UNIT_LENGTH, 320 - 2 * UNIT_LENGTH),
    pygame.Vector2(200 + 2 * UNIT_LENGTH, 320 + UNIT_LENGTH),
    pygame.Vector2(200, 320 + UNIT_LENGTH)]
rotate_about_j = pygame.Vector2(200 + 3 / 2 * UNIT_LENGTH, 320 + 1 / 2 * UNIT_LENGTH)


class Shape:
    def __init__(self):
        self.color = RED
        self.points = j_shape_points
        self.rotate_about = rotate_about_j

    def draw_shape(self, WIN):
        pygame.draw.polygon(WIN, self.color, self.points)
        pygame.draw.polygon(WIN, BLACK, self.points, 1)

    def rotate(self):
        theta = math.pi / 2
        center_x = self.rotate_about.x
        center_y = self.rotate_about.y
        for point in self.points:
            point.update((point.x - center_x) * math.cos(theta) - (point.y - center_y) * math.sin(theta) + center_x,
                (point.x - center_x) * math.sin(theta) + (point.y - center_y) * math.cos(theta) + center_y)

    
