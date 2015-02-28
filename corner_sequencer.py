
class CornerSequencer(object):
    def __init__(self, colors):
        self.colors = colors
        self.position = -1
        proto_positions = {
            0: (1, 13, 10),
            1: (3, 15, 6),
            2: (6, 15, 3), 
            3: (10, 13, 1)
            }
        m_idx = 0
        self.materialized = dict()
        for color in range(0, len(colors)):
            for pos in range(0, len(proto_positions)):
                self.materialized[m_idx] = []
                for idx in range(0, len(proto_positions[pos])):
                    requested_color = idx - color
                    while requested_color < 0:
                        requested_color += len(colors)
                    self.materialized[m_idx] += [self.colors[requested_color] for x in range(0,proto_positions[pos][idx])]
                m_idx += 1

    def cycle(self):
        self.position += 1
        if self.position >= len(self.materialized):
            self.position -= len(self.materialized)
        for color in self.materialized[self.position]:
            yield color
        
