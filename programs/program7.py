# Write a function sin(x,n) to calculate the value of sin(x) using the Taylor series expansion upto n terms.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sin(x, n):
    sum = 0
    for i in range(n + 1):
        sum += ((-1) ** i) * (x ** ((2 * i) + 1)) / factorial((2 * i) + 1)
    return sum


x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

value = sin(x, n)
print(f"The value of sin({x}) for {n} steps is: {value}")
