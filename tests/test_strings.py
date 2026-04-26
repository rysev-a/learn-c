import pytest

def test_get_string_length(configure_test, get_output_content):
    configure_test(["length", "s some long string", "_"])
    assert get_output_content() == "16\n"


@pytest.mark.parametrize("substring, full_string, expected", [
    ("abc", "abc", 1),
    ("abc", "String", 0),
    ("babcbc", "efbababcbcdef", 1),
])
def test_is_substring(configure_test, get_output_content, substring, full_string, expected):
    configure_test(["is_substring", "s " + substring, "s " + full_string])
    assert get_output_content() == str(expected) + "\n"
