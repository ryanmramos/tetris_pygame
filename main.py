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
from grid import Grid
import math
import random

# things to add:
# - add case where a piece CANNOT rotate

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
GREY = (140, 140, 140)

# Unit length
UNIT_LENGTH = 20

# Set windown name
pg.display.set_caption("tetris :)")

def draw_window(placed_shapes, moving_shape, grid):
    WIN.fill(GREY)
    for shape in placed_shapes:
        shape.draw_shape(WIN)
        # print(shape)
    
    moving_shape.draw_shape(WIN)

    # debug circle to see center of rotation
    # pg.draw.circle(WIN, BLACK, (120 + UNIT_LENGTH * moving_shape.rotate_about.x,
    #     120 + UNIT_LENGTH * moving_shape.rotate_about.y), 3)

    grid.draw_grid(WIN)
    
    pg.display.update()

# def fill_bag():
#     bag

def get_random_shape():
    # return O_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    i = random.randint(0, 7)
    if i == 0:
        return I_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    elif i == 1:
        return J_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    elif i == 2:
        return L_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    elif i == 3:
        return O_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    elif i == 4:
        return S_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    elif i == 5:
        return T_shape(UNIT_LENGTH, WIDTH, HEIGHT)
    else:
        return Z_shape(UNIT_LENGTH, WIDTH, HEIGHT)

def place_and_check(placed_shapes, moving_shape):
    moving_shape.moving = False
    placed_shapes.append(moving_shape)
    checked_rows = []
    rows_to_destroy = []
    current_grid = moving_shape.grid.grid
    for cord in moving_shape.grid_cords:
        cordY = int(cord.y)
        if not cordY in checked_rows:
            checked_rows.append(cordY)
            destroy = True
            for i in range(0, moving_shape.grid.num_cols):
                # print(f"row: {i}\ncol: {cordY}")
                if current_grid[cordY][i] == 0:
                    # print(f"not --> {i},{cordY}: {current_grid[cordY][i]}")
                    destroy = False
                    break
            if destroy:
                rows_to_destroy.append(cordY)
                # print(f"destroy row:{cordY}")
            print()
    
    if len(rows_to_destroy) > 0:
        placed_shapes = moving_shape.grid.destroy_rows(placed_shapes, rows_to_destroy)

    return get_random_shape()

def main():
    
    clock = pg.time.Clock()
    run = True
    shapes = []
    placed_shapes = []
    moving_shape = get_random_shape()
    # testShape = Shape(UNIT_LENGTH, WIDTH, HEIGHT)
    frame_num = 1
    down_held = False # keeps track of whether or not down is being held
    left_held = False # keeps track of whether or not left is being held
    right_held = False # keeps track of whether or not right is being held
    grid = Grid(120, 120, 20)
    while(run):
        clock.tick(FPS)
        quick_drop = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

                if event.key == pg.K_UP:
                    moving_shape.rotate()
                
                if event.key == pg.K_LEFT:
                    left_held = True
                    # moving_shape.move_left()

                if event.key == pg.K_RIGHT:
                    right_held = True
                    # moving_shape.move_right()

                if event.key == pg.K_DOWN:
                    down_held = True

                if event.key == pg.K_SPACE:
                    quick_drop = True
            
            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    down_held = False
                if event.key == pg.K_LEFT:
                    left_held = False
                    # moving_shape.move_left()
                if event.key == pg.K_RIGHT:
                    right_held = False
                    # moving_shape.move_right()

        if frame_num % 30 == 0 and not down_held:
            if not moving_shape.move_down():
                moving_shape = place_and_check(placed_shapes, moving_shape)

        elif frame_num % 3 == 0 and down_held:
            if not moving_shape.move_down():
                moving_shape = place_and_check(placed_shapes, moving_shape)

        if quick_drop:
            while moving_shape.move_down():
                continue
            quick_drop = False
            moving_shape = place_and_check(placed_shapes, moving_shape)

        draw_window(placed_shapes, moving_shape, grid)
        
        if frame_num % 5 == 0:
            if left_held:
                moving_shape.move_left()
            if right_held:
                moving_shape.move_right()

        # if frame_num % 20 == 0:
        #     shapes[0].rotate()
        frame_num += 1
        if frame_num >= 60:
            frame_num = 0
            
    pg.quit()

if __name__ == "__main__":
    main()