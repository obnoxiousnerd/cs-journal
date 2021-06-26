# Program to check number of alphabets, digits, vowels, lowercase and uppercase characters.


def parse(text):
    alpha = lc = uc = vowel = digit = 0
    for chr in text:
        if chr.isalpha():
            alpha += 1
            if chr.islower():
                lc += 1
            elif chr.isupper():
                uc += 1
            if chr.lower() in "aeiou":
                vowel += 1
        elif chr.isdigit():
            digit += 1
    return alpha, lc, uc, vowel, digit


with open("lines.txt", "r") as file:
    alpha, lc, uc, vowel, digit = parse(file.read())
    print(f"Number of alphabets: {alpha}")
    print(f"Number of lowercase characters: {lc}")
    print(f"Number of uppercase characters: {uc}")
    print(f"Number of vowels: {vowel}")
    print(f"Number of digits: {digit}")
