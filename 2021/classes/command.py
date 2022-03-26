from classes.direction import Direction


class Command:
    def __init__(self, direction: Direction, distance: int):
        self.direction = direction
        self.distance = distance
