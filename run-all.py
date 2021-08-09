import os
import re
from runner import run

# Regular expression to extract numbers from the filename.
# Example : program10.py -> 10
numbers_regex = re.compile(r"([0-9]+)")
filenums = map(lambda filename: numbers_regex.search(filename) # type: ignore
               [0], os.listdir("programs"))

for prog_num in filenums:
    print(f"Running program {prog_num}...")

    proc_stderr = run(int(prog_num))
    
    if proc_stderr:
        print("Output of STDERR: ")
        print(proc_stderr)
