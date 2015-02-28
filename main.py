import pygame
import sys
import time
import itertools

pygame.init()

size = width, height = (pygame.display.Info().current_w, pygame.display.Info().current_h)
black = 0, 0, 0
speed = [2,2]

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("ball.bmp")
#ballrect = ball.get_rect()

class Square(object):
    issued = 0

    def __init__(self, initial_color, pos, size):
        self.color_ = initial_color
        self.pos_ = pos
        self.size_ = size
        self.num = Square.issued + 0
        Square.issued += 1

    def set_color(self, new_color):
        self.color_ = new_color

    def color(self):
        return self.color_

    def pos(self):
        return self.pos_

    def size(self):
        return (self.size_, self.size_)

    def __repr__(self):
        return "Sq#%d" % self.num

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
                        Color.red, 
                        (self.offset[0] + (col * (self.size + self.padding)),
                         self.offset[1] + (row * (self.size + self.padding))), 
                        self.size))
            self.squares.append(row_array)

    def natural_order(self):
        for row in self.squares:
            for square in row:
                yield square

    def spiral_order(self):
        order = [(2,2),(3,2),(4,2),(4,1),(3,1),(2,1),(1,1),(1,2),(1,3),
                 (2,3),(3,3),(4,3),(5,3),(5,2),(5,1),(5,0),(4,0),(3,0),
                 (2,0),(1,0),(0,0),(0,1),(0,2),(0,3)]

        for each in order:
            row = self.squares[each[1]]
            cell = row[each[0]]
            yield cell

    def update_color_spiral(self, sequencer):
        for square, color in itertools.izip(self.spiral_order(), sequencer.cycle()):
            square.set_color(color)


class Color(object):
    red = (200, 64, 65)
    green = (142, 168, 49)
    blue = (94, 148, 178)
    yellow = (238, 210, 84)
    orange = (248, 165, 66)
    purple = (128, 0, 255)

class ColorSequencer(object):
    def __init__(self, colors, count_for_each, count_total):
        self.materialized = []
        self.colors = colors
        self.count_for_each = count_for_each
        self.count_total = count_total
        self.materialize()

    def materialize(self):
        added = 0
        done = False
        while not done:
            for color in self.colors:
                for count in range(0, self.count_for_each):
                    self.materialized.append(color)
                    added += 1
                    if added >= self.count_total:
                        done = True
                        break
                if done:
                    break

    def rotate(self):
        self.materialized = self.materialized[1:] + [self.materialized[0]]

    def cycle(self):
        while True:
            yield self.materialized[0]
            self.rotate()        

class ColorCycle(object):
    color_cycle_size = 7
    colors = [Color.red, Color.green, Color.blue, Color.yellow, 
              Color.orange, Color.purple]

    def __init__(self):
        self.last_color = Color.red
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

sequencer = ColorSequencer([Color.red, 
                            Color.orange, 
                            Color.yellow, 
                            Color.blue, 
                            Color.green], 5, 24)


while True:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            sys.exit()
    
    screen.fill(black)

    floor.update_color_spiral(sequencer)

    for square in floor.natural_order():
        loc = square.pos()
        size = square.size()
        rect = (loc,size)
        color = square.color()
        pygame.draw.rect(screen, color, rect)

    pygame.display.flip()

    pygame.time.delay(300)

