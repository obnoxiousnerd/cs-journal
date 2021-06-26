import os
import subprocess

input_path = os.path.join(os.getcwd(), "input")
programs_path = os.path.join(os.getcwd(), "programs")
output_path = os.path.join(os.getcwd(), "output")

prog_num = int(input("Enter program number: "))

prog_path = os.path.join(programs_path, f"program{prog_num}.py")
prog_input_path = os.path.join(input_path, f"program{prog_num}.txt")
prog_output_path = os.path.join(output_path, f"program{prog_num}.txt")

process = subprocess.Popen(
    args=["py", prog_path],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

print(f"Running program {prog_num}...")
stdout, stderr = process.communicate(open(prog_input_path, "rb").read())

prog_output_file = open(prog_output_path, "wb")
prog_output_file.write(stdout)

if not stderr:
    print(f"Content of STDERR:")
    print(stderr.decode("utf-8"))

print("Done!")
