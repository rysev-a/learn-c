import ctypes
import pathlib
import subprocess

import pytest


@pytest.fixture
def strings():
    pathlib.Path("./tmp").mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "gcc",
            "-shared",
            "-o",
            "tmp/libstrings.so",
            "library/strings.c",
        ]
    )

    strings_module = ctypes.CDLL("./tmp/libstrings.so")
    strings_module.is_substring.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    strings_module.is_substring.restype = ctypes.c_int

    strings_module.upcase.argtypes = [ctypes.c_char_p]
    strings_module.upcase.restype = ctypes.c_voidp

    return strings_module


def test_is_substr(strings):
    result = strings.is_substring(b"hello", b"hellow")
    assert result == 1


def test_uppercase(strings):
    input = b"hello"
    strings.upcase(input)
    assert input == b"HELLO"
