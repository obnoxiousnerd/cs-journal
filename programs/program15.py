# Read a text file line by line and display each word separated by a #.

with open("lines.txt") as file:
    words = file.read().split(" ")
    print("#".join(words))
