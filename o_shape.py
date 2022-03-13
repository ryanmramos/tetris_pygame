from shapes import Shape
import pygame as pg

START_X = 200 + 20
START_Y = 320

class O_shape(Shape):
    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        super().__init__(UNIT_LENGTH, WIDTH, HEIGHT)
        self.left_most_grid = 5
        self.right_most_grid = 6
        self.points = [pg.Vector2(START_X, START_Y), pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y),
            pg.Vector2(START_X + 2 * UNIT_LENGTH, START_Y + 2 * UNIT_LENGTH),
            pg.Vector2(START_X, START_Y + 2 * UNIT_LENGTH)]
        self.rotate_about = pg.Vector2(START_X + UNIT_LENGTH, START_Y + UNIT_LENGTH)

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
        return # don't need to do anything