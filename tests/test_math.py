def test_math(run_with_args, get_output_content):
    run_with_args("1")
    assert get_output_content() == "30\n"

    run_with_args("2")
    assert get_output_content() == "200\n"




