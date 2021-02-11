# Program to find number of occurences of a substring

sentence = input("Enter a string: ")
substr = input("Enter the substring: ")

words = sentence.split()

occurences = words.count(substr)

if occurences < 0:
    print(f"Substring {substr} is not in the provided string")
else:
    print(f"Number of occurences of {substr}: {occurences}")