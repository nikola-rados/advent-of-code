from turtle import numinput


class Submarine:
    def __init__(self, readings):
        self.readings = readings
        self.simple_increases = 0
        self.deep_increases = 0

    @staticmethod
    def sonar_sweep(readings):
        return len([True for r1, r2 in zip(readings, readings[1:]) if r2 > r1])

    def simple_sonar_sweep(self):
        self.simple_increases = self.sonar_sweep(self.readings)

    def deep_sonar_sweep(self):
        triple_step_sums = [
            sum([r1, r2, r3])
            for r1, r2, r3 in zip(self.readings, self.readings[1:], self.readings[2:])
        ]
        self.deep_increases = self.sonar_sweep(triple_step_sums)
