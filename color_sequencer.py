
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

