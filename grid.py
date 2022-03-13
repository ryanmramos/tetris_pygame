# import main
import pygame as pg

RED = (255, 0, 0)
GREY = (50, 50, 50)

class Grid:
    def __init__(self, START_X, START_Y, UNIT_LENGTH):
        self.num_rows = 20
        self.num_cols = 10
        self.grid = [[0 for r in range(self.num_rows)] for c in range(self.num_cols)]
        self.START_X = START_X
        self.START_Y = START_Y
        self.UNIT_LENGTH = UNIT_LENGTH
        self.color = GREY

    def draw_grid(self, WIN):
        for i in range(1, self.num_rows):
            pg.draw.line(WIN, self.color, (self.START_X, self.START_Y + i * self.UNIT_LENGTH),
                (self.START_X + 10 * self.UNIT_LENGTH, self.START_Y + i * self.UNIT_LENGTH))

        for i in range(1 , self.num_cols):
            pg.draw.line(WIN, self.color, (self.START_X + i * self.UNIT_LENGTH, self.START_Y),
                (self.START_X + i * self.UNIT_LENGTH, self.START_Y + 20 * self.UNIT_LENGTH))
        
        pg.draw.line(WIN, self.color, (self.START_X, self.START_Y),
            (self.START_X, self.START_Y + self.num_rows * self.UNIT_LENGTH), 2)
        pg.draw.line(WIN, self.color, (self.START_X, self.START_Y),
            (self.START_X + self.num_cols * self.UNIT_LENGTH, self.START_Y), 2)
        pg.draw.line(WIN, GREY, (self.START_X + self.num_cols * self.UNIT_LENGTH, self.START_Y),
            (self.START_X + self.num_cols * self.UNIT_LENGTH, self.START_Y + self.num_rows * self.UNIT_LENGTH), 2)
        pg.draw.line(WIN, GREY, (self.START_X, self.START_Y + self.num_rows * self.UNIT_LENGTH),
            (self.START_X + self.num_cols * self.UNIT_LENGTH, self.START_Y + self.num_rows * self.UNIT_LENGTH), 2)

    def test_print(self):
        print("test")

# test = Grid()