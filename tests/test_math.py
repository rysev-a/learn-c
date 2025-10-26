def test_math(run_with_args, get_output_content):
    run_with_args("1", "10", "20")
    assert get_output_content() == "30\n"

    run_with_args("2", "10", "20")
    assert get_output_content() == "200\n"


    run_with_args("4", "55", "48")
    assert get_output_content() == "1\n"

    run_with_args("5", "55", "48")
    assert get_output_content() == "7\n"

