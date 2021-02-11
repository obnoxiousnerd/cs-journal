# Program to find the largest substring which starts with constant


sentence = input("Enter a sentence: ")
words = sentence.split(" ")

CONSONANTS = "bcdfghjklmnpqrstvwxyz"

subs_to_beat = ""

for word in words:
    fc = word[0]
    if fc in CONSONANTS and len(word) > len(subs_to_beat):
        subs_to_beat = word

print(f"The largest substring is {subs_to_beat} with {len(subs_to_beat)} characters")
