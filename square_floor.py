from square import Square
from color import Color
import itertools

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

    def corner_order(self):
        order = [(5,3), (4,3),(5,2), (3,3),(4,2),(5,1), (2,3),(3,2),(4,1),(5,0),
                 (1,3),(2,2),(3,1),(4,0), (0,3),(1,2),(2,1),(3,0),
                 (0,2),(1,1),(2,0), (0,1),(1,0), (0,0)]

        for each in order:
            row = self.squares[each[1]]
            cell = row[each[0]]
            yield cell

    def update_color_sequence(self, sequence, sequencer):
        for square, color in itertools.izip(sequence, sequencer.cycle()):
            square.set_color(color)

