import pygame as pg
import os
from i_shape import I_shape
from j_shape import J_shape
from l_shape import L_shape
from o_shape import O_shape
from s_shape import S_shape
from t_shape import T_shape
from z_shape import Z_shape
from shapes import Shape
import math

# Window size
WIDTH, HEIGHT = 600, 900

# Set window
WIN = pg.display.set_mode((WIDTH, HEIGHT))

# FPS
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)

# Unit length
UNIT_LENGTH = 20

# Set windown name
pg.display.set_caption("tetris :)")

def draw_window(shapes, moving_shape):
    WIN.fill(WHITE)
    for shape in shapes:
        shape.draw_shape(WIN)
        # print(shape)
    
    moving_shape.draw_shape(WIN)
    pg.draw.circle(WIN, BLACK, (moving_shape.rotate_about.x, moving_shape.rotate_about.y), 3)

    pg.draw.line(WIN, RED, (120, 0), (120, HEIGHT))
    pg.draw.line(WIN, RED, (320, 0), (320, HEIGHT))
    
    pg.display.update()

    
def main():
    
    clock = pg.time.Clock()
    run = True
    shapes = []
    moving_shape = Z_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    # testShape = Shape(UNIT_LENGTH, WIDTH, HEIGHT)
    frame_num = 0
    down_held = False # keeps track of whether or not down is being held
    while(run):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

                if event.key == pg.K_UP:
                    moving_shape.rotate(math.pi / 2)
                
                if event.key == pg.K_LEFT:
                    moving_shape.move_left()

                if event.key == pg.K_RIGHT:
                    moving_shape.move_right()

                if event.key == pg.K_DOWN:
                    down_held = True
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    down_held = False

        if frame_num % 30 == 0 and not down_held:
            moving_shape.move_down()
        elif frame_num % 3 == 0 and down_held:
            moving_shape.move_down()

        draw_window(shapes, moving_shape)
        # if frame_num % 20 == 0:
        #     shapes[0].rotate()
        frame_num += 1
        if frame_num >= 60:
            frame_num = 0
            
    pg.quit()

if __name__ == "__main__":
    main()