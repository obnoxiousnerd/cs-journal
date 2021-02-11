# Program to print different patterns using nested loops

n = int(input("Enter number of rows: "))

print("\nPattern1")
# Pattern 1
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * i)
print("\nPattern2")
# Pattern 2
for i in range(n, 0, -1):
    print("*" * i)

print("\nPattern3")
# Pattern 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nPattern4")
# Pattern 4
for i in range(1, n + 1):
    print(f"{i}" * i)

print("\nPattern5")
# Pattern 5
for i in range(65, 65 + (2 * n) + 1, 2):
    for j in range(65, i, 2):
        print(chr(j), end="")
    print()

print("\nPattern6")
# Pattern 6
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)