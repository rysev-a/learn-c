def test_math(configure_test, get_output_content):
    configure_test(["sum", "d 10", "d 20"])
    assert get_output_content() == "30\n"

    configure_test(["multiply", "d 10", "d 20"])
    assert get_output_content() == "200\n"

    configure_test(["quotient", "d 55", "d 48"])
    assert get_output_content() == "1\n"

    configure_test(["remainder", "d 55", "d 48"])
    assert get_output_content() == "7\n"

