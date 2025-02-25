import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(3, 10) == -7
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0