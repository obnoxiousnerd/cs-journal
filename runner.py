import os
import subprocess
import platform
from typing import Union


def run(prog_num: int) -> Union[str, None]:
    """
    Function run runs a program from ./programs with the specified input
    and stores the output into a file with a special format.

    Parameters:
    prog_num: Number to insert in the special filename format.

    Returns:
    Contents of STDERR, if any.

    The format of the filenames is:
    ./programs/program{prog_num}.py - Python Program
    ./input/program{prog_num}.txt   - Input file for the program
    ./output/program{prog_num}.txt  - Output file for the program

    Input files contain a line with content for every `input()` call in the
    program.

    Example:
    * Sample code
    ```python
    input("A number: ")
    input("Anything: ")
    ```
    * Input file:
    ```
    1
    else
    ```
    This example, `1` will be recieved by the first input call
    and `else` by the second.
    """
    input_path = os.path.join(os.getcwd(), "input")
    programs_path = os.path.join(os.getcwd(), "programs")
    output_path = os.path.join(os.getcwd(), "output")

    prog_path = os.path.join(programs_path, f"program{prog_num}.py")
    prog_input_path = os.path.join(input_path, f"program{prog_num}.txt")
    prog_output_path = os.path.join(output_path, f"program{prog_num}.txt")

    prog_patched_path = os.path.join(programs_path, f"program{prog_num}_patched.py")

    patches = open("./patches.py", "r").read()

    with open(prog_patched_path, "w+") as file:
        file.write(patches)
        # To be extra-safe, append newline to seperate patches.
        file.write("\n")
        file.write(open(prog_path, "r").read())
    python_command = "py" if platform.system() == "Windows" else "python3"
    process = subprocess.Popen(
        args=["python3", prog_patched_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    stdout, stderr = process.communicate(open(prog_input_path, "rb").read())
    prog_output_file = open(prog_output_path, "wb")
    prog_output_file.write(stdout)
    os.remove(prog_patched_path)

    if stderr:
        return stderr.decode("utf-8")
