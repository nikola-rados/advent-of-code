from turtle import numinput


class Submarine:
    def __init__(self, readings):
        self.readings = readings
        self.increases = self.sonar_sweep()

    def sonar_sweep(self):
        num_increases = 0
        prev_reading = None

        for reading in self.readings:

            if not prev_reading:
                print(f"{reading} (N/A - no previous measurement)")

            elif reading > prev_reading:
                num_increases += 1
                print(f"{reading} (increased)")

            elif reading < prev_reading:
                print(f"{reading} (decreased)")

            prev_reading = reading

        return num_increases
