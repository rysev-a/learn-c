import ctypes
import pathlib
import subprocess

import pytest


@pytest.fixture
def math():
    pathlib.Path("./tmp").mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "gcc",
            "-shared",
            "-o",
            "tmp/libmath.so",
            "library/math.c",
        ]
    )

    math_module = ctypes.CDLL("./tmp/libmath.so")
    # math sum
    math_module.math_sum.argtypes = [ctypes.c_int, ctypes.c_int]
    math_module.math_sum.restype = ctypes.c_int

    # math multiply
    math_module.math_multiply.argtypes = [ctypes.c_int, ctypes.c_int]
    math_module.math_multiply.restype = ctypes.c_int

    # math quotient
    math_module.math_get_quotient.argtypes = [ctypes.c_int, ctypes.c_int]
    math_module.math_get_quotient.restype = ctypes.c_int

    # math remainder
    math_module.math_get_remainder.argtypes = [ctypes.c_int, ctypes.c_int]
    math_module.math_get_remainder.restype = ctypes.c_int

    return math_module


def test_math_sum(math):
    result = math.math_sum(10, 5)
    assert result == 15


def test_math_multiply(math):
    result = math.math_multiply(10, 5)
    assert result == 50


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (55, 48, 1),
        (10, 5, 2),
        (7, 3, 2),
        (100, 10, 10),
    ],
)
def test_math_get_quotient(math, left, right, expected):
    result = math.math_get_quotient(left, right)
    assert result == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (55, 48, 7),
        (10, 5, 0),
        (7, 3, 1),
        (100, 9, 1),
    ],
)
def test_math_get_remainder(math, left, right, expected):
    result = math.math_get_remainder(left, right)
    assert result == expected
