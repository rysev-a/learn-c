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
    arrays_module.is_sorted_array.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    arrays_module.is_sorted_array.restype = ctypes.c_int

    arrays_module.bubble_sorting.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    arrays_module.bubble_sorting.restype = ctypes.c_void_p

    arrays_module.swap.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int]
    arrays_module.swap.restype = ctypes.c_void_p

    arrays_module.gnome_sort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    arrays_module.gnome_sort.restype = ctypes.c_void_p

    return arrays_module


@pytest.mark.parametrize(
    "python_list, expected",
    [
        ([1, 2, 3, 4, 5], 1),
        ([1, 1, 2, 2, 3], 1),
        ([5, 4, 3, 2, 1], 0),
        ([1, 3, 2, 4, 5], 0),
    ],
)
def test_is_sorted_array(arrays, python_list, expected):
    c_array = (ctypes.c_int * len(python_list))(*python_list)
    result = arrays.is_sorted_array(c_array, len(python_list))
    assert result == expected


@pytest.mark.parametrize(
    "python_list, expected",
    [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([3, 3, 2, 1], [1, 2, 3, 3]),
        ([10, -1, 0, 7], [-1, 0, 7, 10]),
    ],
)
def test_bubble_sorting(arrays, python_list, expected):
    c_array = (ctypes.c_int * len(python_list))(*python_list)
    arrays.bubble_sorting(c_array, len(python_list))
    assert list(c_array) == expected


def test_swap(arrays):
    python_list = [10, 20, 30, 40]
    c_array = (ctypes.c_int * len(python_list))(*python_list)
    arrays.swap(c_array, 1, 3)
    assert list(c_array) == [10, 40, 30, 20]


@pytest.mark.parametrize(
    "python_list, expected",
    [
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([9, 7, 5, 3, 1], [1, 3, 5, 7, 9]),
        ([2, 2, 1, 3, 1], [1, 1, 2, 2, 3]),
    ],
)
def test_gnome_sort(arrays, python_list, expected):
    c_array = (ctypes.c_int * len(python_list))(*python_list)
    arrays.gnome_sort(c_array, len(python_list))
    assert list(c_array) == expected

