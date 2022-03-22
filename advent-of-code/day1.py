from utils import file_to_list
from classes.submarine import Submarine


def day1_challenge(filepath):
    sub = Submarine(file_to_list(filepath))

    print(f"Measurements larger than previous: {sub.increases}")
