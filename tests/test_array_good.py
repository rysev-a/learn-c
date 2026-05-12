import ctypes
import pathlib
import subprocess

import pytest


@pytest.fixture
def arrays():
    pathlib.Path("./tmp").mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "gcc",
            "-shared",
            "-o",
            "tmp/libarrays.so",
            "library/arrays.c",
        ]
    )

    arrays_module = ctypes.CDLL("./tmp/libarrays.so")
    arrays_module.is_sorted_array.argtypes =  [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    arrays_module.is_sorted_array.restype = ctypes.c_int

    return arrays_module


def test_is_sorted_array(arrays):
    python_list = [1, 2, 3, 4, 5]
    c_array = (ctypes.c_int * len(python_list))(*python_list)

    result = arrays.is_sorted_array(c_array, len(python_list))
    assert result == 1


