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

    return math_module


def test_math_sum(math):
    result = math.math_sum(10, 5)
    assert result == 15


def test_math_multiply(math):
    result = math.math_multiply(10, 5)
    assert result == 50
