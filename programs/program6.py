# Program to print numbers in ascending and descending order

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

low, mid, high = 0, 0, 0

if a > b and a > c:
    high = a
    mid, low = (b, c) if b > c else (c, b)
elif b > a and b > c:
    high = b
    mid, low = (a, c) if a > c else (c, a)
else:
    high = c
    mid, low = (a, b) if a > b else (b, a)

print(f"Numbers in ascending order: {low} < {mid} < {high}")
print(f"Numbers in descending order: {high} > {mid} > {low}")