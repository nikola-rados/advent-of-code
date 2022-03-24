import pytest
from classes.submarine import Submarine


@pytest.mark.parametrize("test_readings, expected", [
    ([1,2,3,4,5], 4),
    ([5,4,3,2,1], 0),
    ([1,3,2,5,4], 2)
])
def test_simple_sonar_sweep(test_readings, expected):
    sub = Submarine(test_readings)
    assert sub.simple_sonar_sweep() == expected


@pytest.mark.parametrize("test_readings, expected", [
    ([1,2,3,4,5,6], 3),
    ([5,4,3,2], 0),
    ([1,3,2,5,4,6,2,3,4,2], 3)
])
def test_deep_sonar_sweep(test_readings, expected):
    sub = Submarine(test_readings)
    assert sub.deep_sonar_sweep() == expected
