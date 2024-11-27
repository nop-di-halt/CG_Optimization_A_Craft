import sys
from move import Move
from route import Route


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
        self.__current_route = Route()
        self.can_move = True
        self.__routes = []

    def build_route(self):
        while self.can_move:
            while self.map.can_move_next(self):
                self.__move_next()
            self.__change_direction()

    def get_route(self):
        self.__routes.sort(key=lambda r: r.get_score(), reverse=True)
        return self.__routes[0].get_actions()

    def visited(self, x, y, direction):
        return any(
            (x, y, direction) == m.get_move() for m in self.__current_route.moves
        )

    def get_start(self):
        return (self.start_x, self.start_y)

    def can_set_arrow(self):
        return not any(
            m.x == self.x and m.y == self.y for m in self.__current_route.moves
        )

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
                break

            self.direction = d
            if not self.map.can_move_next(self):
                continue
            self.can_move = True
            prev_x = self.x
            prev_y = self.y
            prev_route = self.__current_route
            self.__current_route = Route(prev_route)
            self.map.set_arrow(self.x, self.y, d)
            self.__current_route.set_arrow(Move(self.x, self.y, self.direction))
            print(
                f"dir...{self.id} {self.x} {self.y} {self.direction}",
                file=sys.stderr,
                flush=True,
            )
            self.build_route()
            for arr in self.__current_route.arrows:
                self.map.reset(arr.x, arr.y)
            self.__routes.append(self.__current_route)
            self.x = prev_x
            self.y = prev_y
            self.__current_route = prev_route

    def __move_next(self):
        self.__current_route.add_move(Move(self.x, self.y, self.direction))
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
