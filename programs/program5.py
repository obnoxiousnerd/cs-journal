# Program to find roots of an equation

import math

a = float(input("Enter value of a: "))
if not a:
    print("a cannot be null in a quadratic equation")
else:
    b = float(input("Enter value of b: "))
    c = float(input("Enter value of c: "))
    print(f"The equation is {a}x² {'+' if b > 0 else ''}{b}x {'+' if c > 0 else ''}{c}")
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        x1 = ((-b + pow(d, 0.5)) / (2 * a)).imag
        x2 = ((-b - pow(d, 0.5)) / (2 * a)).imag
        print(f"The roots are {x1}i and {x2}i")
    elif d == 0:
        x = -b / (2 * a)
        print(f"The root is {x}")
    elif d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"The roots are {x1} and {x2}")
