from classes.submarine import Submarine


def file_to_list(datapath):
    with open(datapath, "r") as f:
        data = [int(line.strip("\n")) for line in f.readlines()]

    return data


def run_challenges(datapath):
    sub = Submarine(readings=file_to_list(datapath))

    sub.simple_sonar_sweep()
    print(f"Part 1: {sub.simple_sonar_sweep()}")

    sub.deep_sonar_sweep()
    print(f"Part 2: {sub.deep_sonar_sweep()}")
