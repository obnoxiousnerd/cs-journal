import os
from runner import run

filenums = [
    # Get the filename (everything before the extension),
    # and then get the number part of the filename.
    int(f.split(".")[0].split("program")[1])
    # For all files in the "program" directory
    for f in os.listdir("programs")
    # If the file is a .py file.
    if f.endswith(".py")
]

for prog_num in filenums:
    print(f"Running program {prog_num}...")

    proc_stderr = run(int(prog_num))

    if proc_stderr:
        print("Output of STDERR: ")
        print(proc_stderr)
