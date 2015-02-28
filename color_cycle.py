from color import Color

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

