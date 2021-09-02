#! /usr/bin/python3
import sys
from runner import run

prog_num = int(sys.argv[1])

print(f"Running program {prog_num}...")

proc_stderr = run(prog_num)

if proc_stderr:
    print("Output of STDERR: ")
    print(proc_stderr)
