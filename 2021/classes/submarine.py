from classes.command import Command
from classes.direction import Direction


class Submarine:
    def __init__(self, readings: list[int] = None, commands: Command = None):
        self.readings = readings if readings else []
        self.commands = commands if commands else []

    def _sonar_sweep(self, readings: list[int]) -> int:
        return len([True for r1, r2 in zip(readings, readings[1:]) if r2 > r1])

    def simple_sonar_sweep(self) -> int:
        return self._sonar_sweep(self.readings)

    def deep_sonar_sweep(self) -> int:
        triple_step_sums = [
            sum([r1, r2, r3])
            for r1, r2, r3 in zip(self.readings, self.readings[1:], self.readings[2:])
        ]
        return self._sonar_sweep(triple_step_sums)

    def simple_position(self) -> int:
        horizontal, depth = 0, 0

        for command in self.commands:
            if command.direction == Direction.down:
                depth += command.distance
            elif command.direction == Direction.up:
                depth -= command.distance
            elif command.direction == Direction.forward:
                horizontal += command.distance

        return horizontal * depth

    def complex_position(self) -> int:
        horizontal, depth, aim = 0, 0, 0

        for command in self.commands:
            if command.direction == Direction.down:
                aim += command.distance
            elif command.direction == Direction.up:
                aim -= command.distance
            elif command.direction == Direction.forward:
                horizontal += command.distance
                depth += aim * command.distance

        return horizontal * depth
