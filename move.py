class Move:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def get_move(self):
        return (self.x, self.y, self.direction)
