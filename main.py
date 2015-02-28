import pygame
import sys
import time

pygame.init()

size = width, height = (pygame.display.Info().current_w, pygame.display.Info().current_h)
black = 0, 0, 0
speed = [2,2]

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("ball.bmp")
#ballrect = ball.get_rect()

class Square(object):
    def __init__(self, initial_color, pos, size):
        self.color_ = initial_color
        self.pos_ = pos
        self.size_ = size

    def set_color(self, new_color):
        self.color_ = new_color

    def pos(self):
        return self.pos_

    def size(self):
        return (self.size_, self.size_)

class SquareFloor(object):
    def __init__(self, rows=4, cols=6, size=80, padding=6, offset=(75,60)):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.padding = padding
        self.offset = offset

        self.create_squares()

    def create_squares(self):
        self.squares = []
        for row in range(0,self.rows):
            row_array = []
            for col in range(0,self.cols):
                row_array.append(Square(
                        ColorCycle.red, 
                        (self.offset[0] + (col * (self.size + self.padding)),
                         self.offset[1] + (row * (self.size + self.padding))), 
                        self.size))
                self.squares.append(row_array)

    def natural_order(self):
        for row in self.squares:
            for square in row:
                yield square

class ColorCycle(object):
    red = (200, 64, 65)
    green = (142, 168, 49)
    blue = (94, 148, 178)
    yellow = (238, 210, 84)
    orange = (248, 165, 66)
    purple = (128, 0, 255)
    color_cycle_size = 7
    colors = [red, green, blue, yellow, orange, purple]

    def __init__(self):
        self.last_color = ColorCycle.red
        self.color_index = 0
        self.last_cycle_value = -1

    def next(self):
        self.last_cycle_value += 1
        if self.last_cycle_value >= ColorCycle.color_cycle_size:
            #rotate to next color
            self.color_index += 1
            if self.color_index >= len(ColorCycle.colors):
                self.color_index = 0
            self.last_color = ColorCycle.colors[self.color_index]
            self.last_cycle_value = 0

        return self.last_color

color_cycle = ColorCycle()
floor = SquareFloor()

while True:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            sys.exit()
    
    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed[1] = -speed[1]

    screen.fill(black)
    #screen.blit(ball, ballrect)
    for row in squares:
        for square in row:
            offset_x = 75
            offset_y = 60
            square_size = 80
            padding = 5
            loc = (offset_x + square[0] * (square_size + padding), 
                   offset_y + square[1] * (square_size + padding))
            size = (square_size, square_size)
            rect = (loc,size)
            color = color_cycle.next()

            pygame.draw.rect(screen, color, rect)

    pygame.display.flip()

    pygame.time.delay(500)

