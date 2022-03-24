from turtle import down
import pytest
from classes.submarine import Submarine


@pytest.mark.parametrize("test_readings, expected", [
    ([1,2,3,4,5], 4),
    ([5,4,3,2,1], 0),
    ([1,3,2,5,4], 2)
])
def test_simple_sonar_sweep(test_readings, expected):
    sub = Submarine(readings=test_readings)
    assert sub.simple_sonar_sweep() == expected


@pytest.mark.parametrize("test_readings, expected", [
    ([1,2,3,4,5,6], 3),
    ([5,4,3,2], 0),
    ([1,3,2,5,4,6,2,3,4,2], 3)
])
def test_deep_sonar_sweep(test_readings, expected):
    sub = Submarine(readings=test_readings)
    assert sub.deep_sonar_sweep() == expected


@pytest.mark.parametrize("test_move_commands, expected", [
    ([("forward", 5), ("up", 2), ("down", 3)], 5),
    ([("up", 5), ("up", 1), ("down", 10), ("forward", 5)], 20),
    ([("down", 5), ("up", 2), ("forward", 10)], 30),
])
def test_simple_position(test_move_commands, expected):
    sub = Submarine(move_commands=test_move_commands)
    assert sub.simple_position() == expected


@pytest.mark.parametrize("test_move_commands, expected", [
    ([("forward", 5), ("up", 2), ("down", 3)], 0),
    ([("up", 5), ("up", 1), ("down", 10), ("forward", 5)], 100),
    ([("down", 5), ("up", 2), ("forward", 10), ("up", 2), ("forward", 2)], 384),
])
def test_complex_position(test_move_commands, expected):
    sub = Submarine(move_commands=test_move_commands)
    assert sub.complex_position() == expected