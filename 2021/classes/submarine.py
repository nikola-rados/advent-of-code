from classes.command import Command
from classes.direction import Direction
import numpy as np
from functools import reduce
import operator


class Submarine:
    def __init__(
        self,
        readings: list[int] = None,
        commands: Command = None,
        consumption=None,
    ):
        self.readings = readings if readings else []
        self.commands = commands if commands else []
        self.consumption = consumption

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

    def _determine_common_bit(self, target: str) -> bin:
        print(self.consumption)
        _, bits_len = self.consumption.shape
        common_bits = ""

        for i in range(bits_len):
            col = list(self.consumption[:, i])
            zeros = col.count(0)
            ones = col.count(1)

            op = {
                "gamma": operator.lt,
                "epsilon": operator.gt,
            }[target]

            if op(zeros, ones):
                common_bits += "0"
            else:
                common_bits += "1"

        return bin(int(common_bits, 2))

    def _bits_to_int(self, bits):
        return int(bits, 2)

    def _calculate_power(self, values):
        return reduce(lambda a, b: self._bits_to_int(a) * self._bits_to_int(b), values)

    def power_consumption(self) -> int:
        gamma = self._determine_common_bit("gamma")
        epsilon = self._determine_common_bit("epsilon")
        return self._calculate_power([gamma, epsilon])
