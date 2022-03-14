from tabnanny import check
import pygame as pg
import os
import math
from grid import Grid

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

class Shape:

    grid = Grid(120, 120, 20)

    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        # self.points = i_shape_points
        # self.rotate_about = rotate_about_i
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.rotate_num = 0

    def draw_shape(self, WIN):
        for cord in self.grid_cords:
            pg.draw.rect(WIN, self.color,
                pg.Rect(120 + cord.x * self.UNIT_LENGTH, 120 + cord.y * self.UNIT_LENGTH,
                self.UNIT_LENGTH, self.UNIT_LENGTH))

    def rotate(self):
        # rotation done in subclass

        if self.left_most_grid < 0:
            difference = -1 * self.left_most_grid
            for cord in self.grid_cords:
                cord.update(cord.x + difference, cord.y)
            self.rotate_about.update(self.rotate_about.x + difference, self.rotate_about.y)
            self.left_most_grid += difference
            self.right_most_grid += difference
        # for cord in self.grid_cords:

        elif self.right_most_grid > self.grid.num_cols - 1:
            difference = self.right_most_grid - (self.grid.num_cols - 1)
            for cord in self.grid_cords:
                cord.update(cord.x - difference, cord.y)
            self.rotate_about.update(self.rotate_about.x - difference, self.rotate_about.y)
            self.left_most_grid -= difference
            self.right_most_grid -= difference

        self.rotate_num += 1
        self.rotate_num %= 4

    def move_down(self):
        for cord in self.grid_cords:
            cordX = int(cord.x)
            cordY = int(cord.y)
            if cord.y + 1 >= self.grid.num_rows or self.grid.grid[cordY + 1][cordX] == 1:
                for set_cord in self.grid_cords:
                    cordX = int(set_cord.x)
                    cordY = int(set_cord.y)
                    self.grid.grid[cordY][cordX] = 1
                return False

        for cord in self.grid_cords:
            cord.update(cord.x, cord.y + 1)
        self.rotate_about.update(self.rotate_about.x, self.rotate_about.y + 1)
        return True

    def move_left(self):
        for cord in self.grid_cords:
            cordX = int(cord.x)
            cordY = int(cord.y)
            # print(f"grid rows = {len(self.grid.grid)}\ngrid cols = {len(self.grid.grid[0])}")
            if cord.x - 1 <= -1 or self.grid.grid[cordY][cordX - 1] == 1:
                return
        
        for cord in self.grid_cords:
            cord.update(cord.x - 1, cord.y)
        self.rotate_about.update(self.rotate_about.x - 1, self.rotate_about.y)
        self.left_most_grid -= 1
        self.right_most_grid -= 1

    def move_right(self):
        for cord in self.grid_cords:
            cordX = int(cord.x)
            cordY = int(cord.y)
            if cord.x + 1 >= self.grid.num_cols or self.grid.grid[cordY][cordX + 1] == 1:
                return
        
        for cord in self.grid_cords:
            cord.update(cord.x + 1, cord.y)
        self.rotate_about.update(self.rotate_about.x + 1, self.rotate_about.y)
        self.left_most_grid += 1
        self.right_most_grid += 1

    
