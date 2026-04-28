import pytest


def test_get_string_length(configure_test, get_output_content):
    configure_test(["length", "s some long string", "_"])
    assert get_output_content() == "16\n"


@pytest.mark.parametrize(
    "substring, full_string, expected",
    [
        ("abc", "abcSdf", 1),
        ("abc", "EFDabcSdf", 1),
        ("abc", "String", 0),
        ("babcbc", "efbababcbcdef", 1),
    ],
)
def test_is_substring(
    configure_test, get_output_content, substring, full_string, expected
):
    configure_test(["is_substring", "s " + substring, "s " + full_string])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "beginning, full_string, expected",
    [
        ("abc", "abc", 1),
        ("abc", "String", 0),
        ("cde", "cdea", 1),
    ],
)
def test_is_beginning(
    configure_test, get_output_content, beginning, full_string, expected
):
    configure_test(["is_beginning", "s " + beginning, "s " + full_string])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abcba", "_", 1),
        ("abc", "_", 0),
        ("abba", "_", 1),
    ],
)
def test_is_palindrome(configure_test, get_output_content, input_string, _, expected):
    configure_test(["is_palindrome", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abc", "_", 1),
        ("ABcd", "_", 0),
        ("werwe", "_", 1),
        ("123", "_", 0),
    ],
)
def test_is_lower_case(configure_test, get_output_content, input_string, _, expected):
    configure_test(["is_lower_case", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"
