from classes.submarine import Submarine


def file_to_pair_list(datapath):
    with open(datapath, "r") as f:
        data = []
        for line in f.readlines():
            direction, distance = line.strip("\n").split(" ")
            data.append((direction, int(distance)))

    return data


def run_challenges(datapath):
    sub = Submarine(move_commands=file_to_pair_list(datapath))

    print(f"Part 1: {sub.simple_position()}")
    print(f"Part 2: {sub.complex_position()}")