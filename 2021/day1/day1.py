from utils import file_to_list
from classes.submarine import Submarine


def run_challenges(datapath):
    sub = Submarine(file_to_list(datapath))

    sub.simple_sonar_sweep()
    print(f"Part 1: {sub.simple_increases}")

    sub.deep_sonar_sweep()
    print(f"Part 2: {sub.deep_increases}")
