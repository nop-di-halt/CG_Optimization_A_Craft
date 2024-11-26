import sys
from move import Move


class Robot:
    directions = ["R", "L", "U", "D"]

    def __init__(self, id, x, y, direction, map):
        self.id = id
        self.x = x
        self.y = y
        self.direction = direction
        self.map = map
        self.start_x = x
        self.start_y = y
        self.moves = []
        self.can_move = True
        self.__route = []

    def build_route(self):
        while self.can_move:
            while self.map.can_move_next(self):
                self.__move_next()
            self.__change_direction()

    def get_route(self):
        return " ".join(self.__route)

    def visited(self, x, y, direction):
        return any((x, y, direction) == m.get_move() for m in self.moves)

    def get_start(self):
        return (self.start_x, self.start_y)

    def can_set_arrow(self):
        return not any(m.x == self.x and m.y == self.y for m in self.moves)

    def __change_direction(self):
        possible_dir = [d for d in Robot.directions if d != self.direction]
        for d in possible_dir:
            print(
                f"{d} can set arrow: {self.id} {self.can_set_arrow()}",
                file=sys.stderr,
                flush=True,
            )
            if not self.can_set_arrow():
                self.can_move = False
                continue

            self.direction = d
            self.can_move = True
            self.map.set_arrow(self.x, self.y, d)
            self.__route.append(f"{self.x} {self.y} {d}")
            print(
                f"dir...{self.id} {self.x} {self.y} {self.direction}",
                file=sys.stderr,
                flush=True,
            )
            break

    def __move_next(self):
        self.moves.append(Move(self.x, self.y, self.direction))
        print(
            f"move...{self.id} {self.x} {self.y} {self.direction}",
            file=sys.stderr,
            flush=True,
        )
        if self.direction == "R":
            self.x = self.x + 1 if self.x < 18 else 0

        if self.direction == "L":
            self.x = self.x - 1 if self.x > 0 else 18

        if self.direction == "U":
            self.y = self.y - 1 if self.y > 0 else 9

        if self.direction == "D":
            self.y = self.y + 1 if self.y < 9 else 0
