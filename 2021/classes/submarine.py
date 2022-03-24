from turtle import numinput


class Submarine:
    def __init__(self, readings = []):
        self.readings = readings

    def _sonar_sweep(self, readings):
        return len([True for r1, r2 in zip(readings, readings[1:]) if r2 > r1])

    def simple_sonar_sweep(self):
        return self._sonar_sweep(self.readings)

    def deep_sonar_sweep(self):
        triple_step_sums = [
            sum([r1, r2, r3])
            for r1, r2, r3 in zip(self.readings, self.readings[1:], self.readings[2:])
        ]
        return self._sonar_sweep(triple_step_sums)
