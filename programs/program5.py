# Program to copy file contents to another file.

filename = input("Enter name of file to copy: ")
destination = input("Enter name of destination file: ")


with open(filename, "r") as src, open(destination, "w+") as dest:
    dest.write(src.read())
    print(f"Copied contents of {filename} to {destination}")

    print(f"Contents of {destination}: ")
    # Move file cursor at the start.
    dest.seek(0)
    # At this point, dest.read() is exactly same as src.read().
    # However, dest.read() is used because of obvious reasons.
    print(dest.read())
