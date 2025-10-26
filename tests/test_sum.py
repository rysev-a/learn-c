import subprocess

def test_math(output_file, get_output_content):
    subprocess.run([f"./{output_file}", "1"])
    assert get_output_content() == "30\n"
    subprocess.run([f"./{output_file}", "2"])
    assert get_output_content() == "Unknown command\n"


