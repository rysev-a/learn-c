import pytest
from uuid import uuid4
import subprocess
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
def run_with_args():
    output_file = f"{uuid4()}.out"
    subprocess.run(
        [
            "gcc",
            "-o",
            output_file,
            "main.c",
        ]
    )
    def run(*args):
        subprocess.run([f"./{output_file}", *args])

    yield run
    os.remove(output_file)
    os.remove("output.txt")



@pytest.fixture()
def get_output_content():
    def read_content_from_file():
        with open("output.txt", "r") as f:
            content = f.read()
        return content
    return read_content_from_file
