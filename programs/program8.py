# Program to print number of letters, digits, lowercase,
# uppercase, and special characters

sentence = input("Enter a sentence: ")
spaces = d = lc = uc = sc = 0

for chr in sentence:
    if chr.islower():
        lc += 1
    elif chr.isupper():
        uc += 1
    elif chr.isdigit():
        d += 1
    elif chr.isspace():
        spaces += 1
    else:
        sc += 1

print(f"No. of lowercase characters : {lc}")
print(f"No. of uppercase characters : {uc}")
print(f"No. of special characters : {sc}")
print(f"No. of digits : {d}")
print(f"No. of spaces : {spaces}")