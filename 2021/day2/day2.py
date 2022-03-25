from classes.submarine import Submarine
from classes.command import Command
from classes.direction import Direction


def file_to_command_list(datapath: str) -> list[Command]:
    with open(datapath, "r") as f:
        data = []
        for line in f.readlines():
            direction, distance = line.strip("\n").split(" ")
            data.append(Command(Direction[direction], int(distance)))

    return data


def run_challenges(datapath: str):
    sub = Submarine(commands=file_to_command_list(datapath))

    print(f"Part 1: {sub.simple_position()}")
    print(f"Part 2: {sub.complex_position()}")
