# Program to check if a number is palindrome and to
# calculate the sum and product of the digits

n = int(input("Enter a number: "))
n_copy = n
n_rev = 0
prod, sum = 1, 0

while n_copy > 0:
    # Extract the digit
    digit = n_copy % 10
    sum += digit
    prod *= digit
    n_rev = n_rev * 10 + digit
    # Remove the extracted digit
    n_copy //= 10

if n == n_rev:
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")

print(f"reverse of n : {n_rev}")
print(f"sum of digits : {sum}")
print(f"product of digits : {prod}")