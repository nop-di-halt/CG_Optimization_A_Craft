import numpy as np


class Map:
    def __init__(self):
        self.map = np.empty((19, 10), np.str_)

    def update_map(self, x_row, y):
        for i, ch in enumerate(x_row):
            self.map[i, y] = ch

    def get_at(self, x, y):
        return self.map[x, y]

    def set_arrow(self, x, y, direction):
        self.map[x, y] = direction

    def reset(self, x, y):
        self.map[x, y] = "."

    def can_move_next(self, robot):
        x = robot.x
        y = robot.y
        current_direction = robot.direction
        if self.map[x, y] in "RLUD":
            robot.direction = self.map[x, y]

        direction = robot.direction

        if direction == "R":
            x = x + 1 if x < 18 else 0

        if direction == "L":
            x = x - 1 if x > 0 else 18

        if direction == "U":
            y = y - 1 if y > 0 else 9

        if direction == "D":
            y = y + 1 if y < 9 else 0

        if self.map[x, y] in "RLUD":
            direction = self.map[x, y]

        if robot.visited(x, y, direction):
            robot.can_move = False
            robot.direction = current_direction
            return False

        if robot.has_arrow(x, y):
            robot.can_move = False
            robot.direction = current_direction
            return False

        return self.map[x, y] != "#"
