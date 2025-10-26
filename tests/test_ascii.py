def test_char_code(run_with_args, get_output_content):
    run_with_args("3", "A")
    assert get_output_content() == f"ASCII-code A={ord('A')}\n"




