import pytest
import subprocess
from pathlib import Path

@pytest.fixture()
def configure_test():
    def configure(input_content):
        Path("./tmp").mkdir(parents=True, exist_ok=True)
        with open("./tmp/input.txt", "w") as f:
            for input_string in input_content:
                f.write(input_string + "\n")
        # compile and run
        subprocess.run(
            [
                "gcc",
                "-Wall",
                "-fsanitize=address",
                "-o",
                "./tmp/a.out",
                "main.c",
            ]
        )
        subprocess.run(["./tmp/a.out"])
    return configure

@pytest.fixture()
def get_output_content():
    def read_content_from_file():
        with open("./tmp/output.txt", "r") as f:
            content = f.read()
        return content
    yield read_content_from_file

