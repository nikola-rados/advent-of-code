import numpy as np
from classes.submarine import Submarine
import constants


def file_to_np(datapath: str) -> np.array:
    with open(datapath, constants.READ) as f:
        data = np.array(
            [
                [int(bit) for bit in bits.strip(constants.NEWLINE)]
                for bits in f.readlines()
            ],
            dtype=object,
        )

    return data


def run_challenges(datapath: str):
    sub = Submarine(consumption=file_to_np(datapath))

    print(f"Part 1: {sub.power_consumption()}")
