import pytest
import subprocess
from uuid import uuid4
import os

@pytest.fixture()
def output_file():
    output_file = f"{uuid4()}.out"
    subprocess.run(
        [
            "gcc",
            "-o",
            output_file,
            "main.c",
        ]
    )

    yield output_file
    os.remove(output_file)
    os.remove("output.txt")


@pytest.fixture()
def get_output_content():
    def read_content_from_file():
        with open("output.txt", "r") as f:
            content = f.read()
        return content
    return read_content_from_file
