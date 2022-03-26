from turtle import down
import pytest
from classes.submarine import Submarine
from classes.command import Command
from classes.direction import Direction


@pytest.mark.parametrize(
    "test_readings, expected",
    [([1, 2, 3, 4, 5], 4), ([5, 4, 3, 2, 1], 0), ([1, 3, 2, 5, 4], 2)],
)
def test_simple_sonar_sweep(test_readings: list[int], expected: int):
    sub = Submarine(readings=test_readings)
    assert sub.simple_sonar_sweep() == expected


@pytest.mark.parametrize(
    "test_readings, expected",
    [([1, 2, 3, 4, 5, 6], 3), ([5, 4, 3, 2], 0), ([1, 3, 2, 5, 4, 6, 2, 3, 4, 2], 3)],
)
def test_deep_sonar_sweep(test_readings: list[int], expected: int):
    sub = Submarine(readings=test_readings)
    assert sub.deep_sonar_sweep() == expected


@pytest.mark.parametrize(
    "test_commands, expected",
    [
        (
            [
                Command(Direction.forward, 5),
                Command(Direction.up, 2),
                (Command(Direction.down, 3)),
            ],
            5,
        ),
        (
            [
                Command(Direction.up, 5),
                Command(Direction.up, 1),
                Command(Direction.down, 10),
                Command(Direction.forward, 5),
            ],
            20,
        ),
        (
            [
                Command(Direction.down, 5),
                Command(Direction.up, 2),
                Command(Direction.forward, 10),
            ],
            30,
        ),
    ],
)
def test_simple_position(test_commands: list[Command], expected: int):
    sub = Submarine(commands=test_commands)
    assert sub.simple_position() == expected


@pytest.mark.parametrize(
    "test_commands, expected",
    [
        (
            [
                Command(Direction.forward, 5),
                Command(Direction.up, 2),
                Command(Direction.down, 3),
            ],
            0,
        ),
        (
            [
                Command(Direction.up, 5),
                Command(Direction.up, 1),
                Command(Direction.down, 10),
                Command(Direction.forward, 5),
            ],
            100,
        ),
        (
            [
                Command(Direction.down, 5),
                Command(Direction.up, 2),
                Command(Direction.forward, 10),
                Command(Direction.up, 2),
                Command(Direction.forward, 2),
            ],
            384,
        ),
    ],
)
def test_complex_position(test_commands: list[Command], expected: int):
    sub = Submarine(commands=test_commands)
    assert sub.complex_position() == expected
