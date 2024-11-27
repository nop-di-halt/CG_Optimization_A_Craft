class Route:
    def __init__(self, route=[]):
        if route:
            self.moves = route.moves.copy()
            self.arrows = route.arrows.copy()
        else:
            self.moves = []
            self.arrows = []

    def add_move(self, move):
        self.moves.append(move)

    def set_arrow(self, move):
        self.arrows.append(move)

    def get_score(self):
        return len(self.moves)

    def get_actions(self):
        return " ".join([f"{m.x} {m.y} {m.direction}" for m in self.arrows])
