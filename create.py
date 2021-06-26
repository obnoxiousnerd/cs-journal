num = int(input("Enter the program number: "))
description = input("Enter program description: ")


def touch(filename, content):
    file = open(filename, "w")
    if content:
        file.write(content)


touch(f"./input/program{num}.txt", "")
touch(f"./programs/program{num}.py", f"# {description}.\n")
print("Created files")

with open("index.txt", "a") as index_file:
    index_file.write(f"{num}: {description}\n")
print("Updated index")
