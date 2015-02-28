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

