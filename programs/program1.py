# Program to check if a number is palindrome, or prime, or both.


def is_prime(num):
    # Check till num/2 because after that it is impossible to find a factor.
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    rev = 0
    div = num
    while div > 0:
        digit = div % 10
        # Add the last digit multiplied by 10 to the reverse number.
        rev = rev * 10 + digit
        div //= 10
    return rev == num


num = int(input("Enter a number: "))
print(f"Is {num} prime? : {is_prime(num)}")
print(f"Is {num} palindrome? : {is_palindrome(num)}")
