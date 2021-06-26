# Program to extract all the digits and find the sum

sentence = input("Enter a string with numbers: ")

# List comprehension
numbers = [int(x) for x in sentence if x.isdigit()]

sum = 0
for num in numbers:
    sum += num

print(f"Number of digits : {len(numbers)}")
print(f"Sum of digits : {sum}")