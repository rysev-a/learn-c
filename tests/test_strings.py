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


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abc", "_", 1),
        ("ABcd", "_", 1),
        ("werwe", "_", 1),
        ("123", "_", 0),
        ("abcd123", "_", 1),
        ("abcd_123", "_", 0),
        ("abcd-123", "_", 0),
        ("abcd#$", "_", 0),
        ("abcd123efg", "_", 1),
    ],
)
def test_is_identifier(configure_test, get_output_content, input_string, _, expected):
    configure_test(["is_identifier", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abc", "_", "ABC"),
        ("ABcd", "_", "ABCD"),
        ("werwe", "_", "WERWE"),
        ("123", "_", "123"),
        ("abcd123", "_", "ABCD123"),
    ],
)
def test_upcase(configure_test, get_output_content, input_string, _, expected):
    configure_test(["upcase", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abc", "_", "ABC"),
        ("ABcd", "_", "abCD"),
        ("werwe", "_", "WERWE"),
        ("123", "_", "123"),
        ("abcd123", "_", "ABCD123"),
    ],
)
def test_swap_case(configure_test, get_output_content, input_string, _, expected):
    configure_test(["swap_case", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, _, expected",
    [
        ("abc", "_", "cba"),
        ("ABcd", "_", "dcBA"),
        ("werwe", "_", "ewrew"),
        ("123", "_", "321"),
        ("abcd123", "_", "321dcba"),
    ],
)
def test_reverse(configure_test, get_output_content, input_string, _, expected):
    configure_test(["reverse", "s " + input_string, "s " + _])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, count, expected",
    [
        ("abc", 3, "abcabcabc"),
        ("ABcd", 2, "ABcdABcd"),
        ("werwe", 1, "werwe"),
        ("123", 4, "123123123123"),
        ("abcd123", 2, "abcd123abcd123"),
    ],
)
def test_duplicate(configure_test, get_output_content, input_string, count, expected):
    configure_test(["duplicate", "s " + input_string, "d " + str(count)])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "left_string, right_string, expected",
    [
        ("abc", "def", "abcdef"),
        ("ABcd", "efg", "ABcdefg"),
        ("werwe", "xyz", "werwexyz"),
        ("123", "456", "123456"),
        ("abcd123", "efg", "abcd123efg"),
        ("0", "123", "0123"),
        ("012", "3", "0123"),
    ],
)
def test_concat_strings(
    configure_test, get_output_content, left_string, right_string, expected
):
    configure_test(["concat_strings", "s " + left_string, "s " + right_string])
    assert get_output_content() == str(expected) + "\n"


@pytest.mark.parametrize(
    "input_string, index, expected",
    [
        ("abc", 0, "bc"),
        ("ABcd", 1, "Acd"),
        ("werwe", 2, "wewe"),
        ("1234567", 3, "123567"),
        ("abcd123", 2, "abd123"),
        ("012", 1, "02"),
    ],
)
def test_delete_symbol(
    configure_test, get_output_content, input_string, index, expected
):
    configure_test(["delete_symbol", "s " + input_string, "d " + str(index)])
    assert get_output_content() == str(expected) + "\n"
