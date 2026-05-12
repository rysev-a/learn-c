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
        ],
        check=True,
    )

    strings_module = ctypes.CDLL("./tmp/libstrings.so")
    strings_module.get_string_length.argtypes = [ctypes.c_char_p]
    strings_module.get_string_length.restype = ctypes.c_int

    strings_module.is_substring.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    strings_module.is_substring.restype = ctypes.c_int

    strings_module.is_beginning.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    strings_module.is_beginning.restype = ctypes.c_int

    strings_module.is_palindrome.argtypes = [ctypes.c_char_p]
    strings_module.is_palindrome.restype = ctypes.c_int

    strings_module.is_lower_case.argtypes = [ctypes.c_char_p]
    strings_module.is_lower_case.restype = ctypes.c_int

    strings_module.is_identifier.argtypes = [ctypes.c_char_p]
    strings_module.is_identifier.restype = ctypes.c_int

    strings_module.upcase.argtypes = [ctypes.c_char_p]
    strings_module.upcase.restype = ctypes.c_void_p

    strings_module.swap_case.argtypes = [ctypes.c_char_p]
    strings_module.swap_case.restype = ctypes.c_void_p

    strings_module.reverse.argtypes = [ctypes.c_char_p]
    strings_module.reverse.restype = ctypes.c_void_p

    strings_module.duplicate_string.argtypes = [ctypes.c_char_p, ctypes.c_int]
    strings_module.duplicate_string.restype = ctypes.c_char_p

    strings_module.concat_strings.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    strings_module.concat_strings.restype = ctypes.c_char_p

    strings_module.delete_symbol.argtypes = [ctypes.c_char_p, ctypes.c_int]
    strings_module.delete_symbol.restype = ctypes.c_char_p

    strings_module.title_case.argtypes = [ctypes.c_char_p]
    strings_module.title_case.restype = ctypes.c_char_p

    return strings_module


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"", 0),
        (b"a", 1),
        (b"abc", 3),
        (b"some long string", 16),
        (b"  leading and trailing  ", 24),
        (b"line1\nline2", 11),
        (b"1234567890", 10),
        (b"with-symbols_#%!", 16),
    ],
)
def test_get_string_length(strings, input_text, expected):
    result = strings.get_string_length(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "substring, full_string, expected",
    [
        (b"lo", b"hello", 1),
        (b"world", b"hello", 0),
        (b"aba", b"cababd", 1),
        (b"abc", b"abcSdf", 1),
        (b"abc", b"EFDabcSdf", 1),
        (b"abc", b"String", 0),
        (b"babcbc", b"efbababcbcdef", 1),
    ],
)
def test_is_substring(strings, substring, full_string, expected):
    result = strings.is_substring(substring, full_string)
    assert result == expected


@pytest.mark.parametrize(
    "beginning, full_string, expected",
    [
        (b"abc", b"abc", 1),
        (b"abc", b"String", 0),
        (b"cde", b"cdea", 1),
    ],
)
def test_is_beginning(strings, beginning, full_string, expected):
    result = strings.is_beginning(beginning, full_string)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abcba", 1),
        (b"abc", 0),
        (b"abba", 1),
    ],
)
def test_is_palindrome(strings, input_text, expected):
    result = strings.is_palindrome(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abc", 1),
        (b"ABcd", 0),
        (b"werwe", 1),
        (b"123", 0),
    ],
)
def test_is_lower_case(strings, input_text, expected):
    result = strings.is_lower_case(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abc", 1),
        (b"ABcd", 1),
        (b"werwe", 1),
        (b"123", 0),
        (b"abcd123", 1),
        (b"abcd_123", 0),
        (b"abcd-123", 0),
        (b"abcd#$", 0),
        (b"abcd123efg", 1),
    ],
)
def test_is_identifier(strings, input_text, expected):
    result = strings.is_identifier(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abc123", b"ABC123"),
        (b"AlreadyUP", b"ALREADYUP"),
        (b"mIxEd", b"MIXED"),
        (b"ABcd", b"ABCD"),
        (b"werwe", b"WERWE"),
        (b"123", b"123"),
        (b"abcd123", b"ABCD123"),
    ],
)
def test_upcase(strings, input_text, expected):
    input_string = ctypes.create_string_buffer(input_text)
    strings.upcase(input_string)
    assert input_string.value == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"hello world", b"Hello World"),
        (b"already Title", b"Already Title"),
        (b"a  b", b"A  B"),
    ],
)
def test_title_case(strings, input_text, expected):
    result = strings.title_case(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abc", b"ABC"),
        (b"ABcd", b"abCD"),
        (b"123", b"123"),
        (b"werwe", b"WERWE"),
        (b"abcd123", b"ABCD123"),
    ],
)
def test_swap_case(strings, input_text, expected):
    input_string = ctypes.create_string_buffer(input_text)
    strings.swap_case(input_string)
    assert input_string.value == expected


@pytest.mark.parametrize(
    "input_text, expected",
    [
        (b"abc", b"cba"),
        (b"ABcd", b"dcBA"),
        (b"123", b"321"),
        (b"werwe", b"ewrew"),
        (b"abcd123", b"321dcba"),
    ],
)
def test_reverse(strings, input_text, expected):
    input_string = ctypes.create_string_buffer(input_text)
    strings.reverse(input_string)
    assert input_string.value == expected


@pytest.mark.parametrize(
    "input_text, count, expected",
    [
        (b"abc", 3, b"abcabcabc"),
        (b"ABcd", 2, b"ABcdABcd"),
        (b"123", 4, b"123123123123"),
        (b"werwe", 1, b"werwe"),
        (b"abcd123", 2, b"abcd123abcd123"),
    ],
)
def test_duplicate_string(strings, input_text, count, expected):
    result = strings.duplicate_string(input_text, count)
    assert result == expected


@pytest.mark.parametrize(
    "left, right, expected",
    [
        (b"abc", b"def", b"abcdef"),
        (b"ABcd", b"efg", b"ABcdefg"),
        (b"123", b"456", b"123456"),
        (b"werwe", b"xyz", b"werwexyz"),
        (b"abcd123", b"efg", b"abcd123efg"),
        (b"0", b"123", b"0123"),
        (b"012", b"3", b"0123"),
    ],
)
def test_concat_strings(strings, left, right, expected):
    result = strings.concat_strings(left, right)
    assert result == expected


@pytest.mark.parametrize(
    "input_text, index, expected",
    [
        (b"abc", 0, b"bc"),
        (b"ABcd", 1, b"Acd"),
        (b"1234567", 3, b"123567"),
        (b"werwe", 2, b"wewe"),
        (b"abcd123", 2, b"abd123"),
        (b"012", 1, b"02"),
    ],
)
def test_delete_symbol(strings, input_text, index, expected):
    result = strings.delete_symbol(input_text, index)
    assert result == expected
