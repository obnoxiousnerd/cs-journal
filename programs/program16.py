# Remove all the lines that contain the character ‘a’ in a file and write it to another file.

with open("lines.txt") as file:
    lines = file.readlines()
    filtered_lines = [line for line in lines if "a" in line.lower()]
    with open("lines-with-a.txt", "w") as to_file:
        to_file.writelines(filtered_lines)

    print("Filtered lines: ")
    for line in filtered_lines:
        print(line, end="")
