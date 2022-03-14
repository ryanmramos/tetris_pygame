from shapes import Shape
import pygame as pg

START_X = 200
START_Y = 320

ORANGE = (255, 215, 0)

class L_shape(Shape):
    def __init__(self, UNIT_LENGTH, WIDTH, HEIGHT):
        self.color = ORANGE
        self.left_most_grid = 3
        self.right_most_grid = 5
        self.UNIT_LENGTH = UNIT_LENGTH
        self.grid_cords = [pg.Vector2(5, 0), pg.Vector2(3, 1), pg.Vector2(4, 1), pg.Vector2(5, 1)]
        self.rotate_about = pg.Vector2(4.5, 1.5)
        super().__init__(UNIT_LENGTH, WIDTH, HEIGHT)

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
        if self.rotate_num == 0:
            self.grid_cords[0].update(self.grid_cords[0].x, self.grid_cords[0].y + 2)
            self.grid_cords[1].update(self.grid_cords[1].x + 1, self.grid_cords[1].y - 1)
            self.grid_cords[3].update(self.grid_cords[3].x - 1, self.grid_cords[3].y + 1)
            self.left_most_grid += 1
        elif self.rotate_num == 1:
            self.grid_cords[0].update(self.grid_cords[0].x - 2, self.grid_cords[0].y)
            self.grid_cords[1].update(self.grid_cords[1].x + 1, self.grid_cords[1].y + 1)
            self.grid_cords[3].update(self.grid_cords[3].x - 1, self.grid_cords[3].y - 1)
            self.left_most_grid -= 1
        elif self.rotate_num == 2:
            self.grid_cords[0].update(self.grid_cords[0].x, self.grid_cords[0].y - 2)
            self.grid_cords[1].update(self.grid_cords[1].x - 1, self.grid_cords[1].y + 1)
            self.grid_cords[3].update(self.grid_cords[3].x + 1, self.grid_cords[3].y - 1)
            self.right_most_grid -= 1
        else:
            self.grid_cords[0].update(self.grid_cords[0].x + 2, self.grid_cords[0].y)
            self.grid_cords[1].update(self.grid_cords[1].x - 1, self.grid_cords[1].y -1)
            self.grid_cords[3].update(self.grid_cords[3].x + 1, self.grid_cords[3].y + 1)
            self.right_most_grid += 1

        super().rotate()