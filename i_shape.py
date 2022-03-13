from shapes import Shape
import pygame as pg

START_X = 200
START_Y = 320

class I_shape(Shape):
    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        super().__init__(UNIT_LENGTH, WIDTH, HEIGHT)
        self.left_most_grid = 4
        self.right_most_grid = 7
        self.points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + 4 * UNIT_LENGTH, START_Y),
            pg.Vector2(START_X + 4 * UNIT_LENGTH, START_Y + UNIT_LENGTH),
            pg.Vector2(START_X, START_Y + UNIT_LENGTH)]
        self.rotate_about = pg.Vector2(START_X + 2 * UNIT_LENGTH,
            START_Y + UNIT_LENGTH)

    def move_left(self):
        if self.left_most_grid > 0:
            self.left_most_grid -=1
            self.right_most_grid -= 1
            super().move_left()

    def move_right(self):
        if self.right_most_grid < 9:
            self.left_most_grid += 1
            self.right_most_grid += 1
            super().move_right()

    def rotate(self, theta):
        if self.rotate_num == 0:
            self.left_most_grid += 2
            self.right_most_grid -= 1
        elif self.rotate_num == 1:
            self.left_most_grid -= 2
            self.right_most_grid += 1
        elif self.rotate_num == 2:
            self.left_most_grid += 1
            self.right_most_grid -= 2
        else:
            self.left_most_grid -= 1
            self.right_most_grid += 2

        if self.left_most_grid < 0:
            difference = -1 * self.left_most_grid
            for i in range(0, difference):
                self.move_right()

        elif self.right_most_grid > 9:
            difference = self.right_most_grid - 9
            for i in range(0, difference):
                self.move_left()

        super().rotate(theta)