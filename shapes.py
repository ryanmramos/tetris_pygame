import pygame as pg
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
START_X = 200
START_Y = 320

# I SHAPE
i_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y + 4 * UNIT_LENGTH),
    pg.Vector2(START_X, START_Y + 4 * UNIT_LENGTH)]
rotate_about_i = pg.Vector2(START_X, START_Y + 2 * UNIT_LENGTH)

# J SHAPE
j_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y - 2 * UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y - 2 * UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y + UNIT_LENGTH),
    pg.Vector2(START_X, START_Y + UNIT_LENGTH)]
rotate_about_j = pg.Vector2(START_X + 3 / 2 * UNIT_LENGTH, START_Y - 1 / 2 * UNIT_LENGTH)

# L SHAPE
l_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X, START_Y - 3 * UNIT_LENGTH),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y - 3 * UNIT_LENGTH),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y)]
rotate_about_l = pg.Vector2(START_X + 1 / 2 * UNIT_LENGTH, START_Y - 3 / 2 * UNIT_LENGTH)

# O SHAPE
o_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y + 2 * UNIT_LENGTH), pg.Vector2(START_X, START_Y + 2 * UNIT_LENGTH)]
rotate_about_o = pg.Vector2(START_X + UNIT_LENGTH, START_Y + UNIT_LENGTH)

# S SHAPE
s_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y), pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y + UNIT_LENGTH), pg.Vector2(START_X, START_Y + UNIT_LENGTH)]
rotate_about_s = pg.Vector2(START_X + 3 / 2 * UNIT_LENGTH, START_Y + 1 / 2 * UNIT_LENGTH)

# T SHAPE
t_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y - UNIT_LENGTH),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y), pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y + UNIT_LENGTH), pg.Vector2(START_X, START_Y + UNIT_LENGTH)]
rotate_about_t = pg.Vector2(START_X + 3 / 2 * UNIT_LENGTH, START_Y + 1 / 2 * UNIT_LENGTH)

# Z SHAPE
z_shape_points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y),
    pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y + UNIT_LENGTH),
    pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y + UNIT_LENGTH),
    pg.Vector2(START_X + 3 * UNIT_LENGTH, START_Y + 2 * UNIT_LENGTH),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y + 2 * UNIT_LENGTH),
    pg.Vector2(START_X + UNIT_LENGTH, START_Y + UNIT_LENGTH), pg.Vector2(START_X, START_Y + UNIT_LENGTH)]
rotate_about_z = pg.Vector2(START_X + 3 /2 * UNIT_LENGTH, START_Y + 3 / 2 * UNIT_LENGTH)


class Shape:
    def __init__(self):
        self.color = RED
        self.points = z_shape_points
        self.rotate_about = rotate_about_z
    def draw_shape(self, WIN):
        pg.draw.polygon(WIN, self.color, self.points)
        pg.draw.polygon(WIN, BLACK, self.points, 1)

    def rotate(self):
        theta = math.pi / 2
        center_x = self.rotate_about.x
        center_y = self.rotate_about.y
        for point in self.points:
            point.update((point.x - center_x) * math.cos(theta) - (point.y - center_y) * math.sin(theta) + center_x,
                (point.x - center_x) * math.sin(theta) + (point.y - center_y) * math.cos(theta) + center_y)

    
