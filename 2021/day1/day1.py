from classes.submarine import Submarine
import constants


def file_to_list(datapath: str) -> list[int]:
    with open(datapath, constants.READ) as f:
        data = [int(line.strip(constants.NEWLINE)) for line in f.readlines()]

    return data


def run_challenges(datapath: str):
    sub = Submarine(readings=file_to_list(datapath))

    sub.simple_sonar_sweep()
    print(f"Part 1: {sub.simple_sonar_sweep()}")

    sub.deep_sonar_sweep()
    print(f"Part 2: {sub.deep_sonar_sweep()}")
