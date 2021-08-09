with open("lines.txt", "r") as file:
    lines = file.readlines()
    print(f"The file has {len(lines)} lines")
    print("File contents line by line: ")
    for line in lines:
        # readlines does not remove line feed character so strip them while printing.
        print(line.strip())
