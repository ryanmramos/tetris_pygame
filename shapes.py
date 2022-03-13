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

# Shapes - starting positions
UNIT_LENGTH = 20
START_X = 200
START_Y = 200

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
    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        self.color = RED
        # self.points = i_shape_points
        # self.rotate_about = rotate_about_i
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rotate_num = 0

    def draw_shape(self, WIN):
        pg.draw.polygon(WIN, self.color, self.points)
        pg.draw.polygon(WIN, BLACK, self.points, 1)

    def rotate(self, theta):
        center_x = self.rotate_about.x
        center_y = self.rotate_about.y
        for point in self.points:
            point.update((point.x - center_x) * math.cos(theta) - (point.y - center_y) * math.sin(theta) + center_x,
                (point.x - center_x) * math.sin(theta) + (point.y - center_y) * math.cos(theta) + center_y)
        self.rotate_num += 1
        self.rotate_num %= 4

    def move_down(self):
        for point in self.points:
            point.update(point.x, point.y + UNIT_LENGTH)
        self.rotate_about.update(self.rotate_about.x, self.rotate_about.y + UNIT_LENGTH)

    def move_left(self):
        for point in self.points:
            point.update(point.x - UNIT_LENGTH, point.y)
        self.rotate_about.update(self.rotate_about.x - UNIT_LENGTH, self.rotate_about.y)

    def move_right(self):
        for point in self.points:
            point.update(point.x + UNIT_LENGTH, point.y)
        self.rotate_about.update(self.rotate_about.x + UNIT_LENGTH, self.rotate_about.y)

    
