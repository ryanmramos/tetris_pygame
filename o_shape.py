from shapes import Shape
import pygame as pg

START_X = 200 + 20
START_Y = 320

YELLOW = (255, 255, 0)

class O_shape(Shape):
    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        super().__init__(UNIT_LENGTH, WIDTH, HEIGHT)
        self.color = YELLOW
        self.left_most_grid = 4
        self.right_most_grid = 5
        self.UNIT_LENGTH = UNIT_LENGTH
        self.grid_cords = [pg.Vector2(4, 0), pg.Vector2(5, 0), pg.Vector2(4, 1), pg.Vector2(5, 1)]
        self.rotate_about = pg.Vector2(5, 1)

    # def move_left(self):
    #     if self.left_most_grid > 0:
    #         self.left_most_grid -=1
    #         self.right_most_grid -= 1
    #         super().move_left()

    # def move_right(self):
    #     if self.right_most_grid < 9:
    #         self.left_most_grid += 1
    #         self.right_most_grid += 1
    #         super().move_right()

    def rotate(self):
        return # don't need to do anything