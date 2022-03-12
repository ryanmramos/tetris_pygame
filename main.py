import pygame
import os
from shapes import Shape

# Window size
WIDTH, HEIGHT = 600, 900

# Set window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# FPS
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
YELLOW = (255, 255, 0)

# Set windown name
pygame.display.set_caption("tetris :)")

def draw_window(shapes):
    WIN.fill(WHITE)
    for shape in shapes:
        shape.draw_shape(WIN)
        # print(shape)
    
    pygame.display.update()

    
def main():
    
    clock = pygame.time.Clock()
    run = True
    shapes = []
    testShape = Shape()
    shapes.append(testShape)
    frame_num = 0
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window(shapes)
        if frame_num % 20 == 0:
            shapes[0].rotate()
        frame_num += 1
        if frame_num >= 60:
            frame_num = 0
            
    pygame.quit()

if __name__ == "__main__":
    main()