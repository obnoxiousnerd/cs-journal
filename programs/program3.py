# Program to count number of occurences of a given word from a file.

with open("lines.txt", "r") as file:
    content = file.read()
    word = input("Enter the word: ").lower()

    words = content.lower().split()
    print(f"Number of words: {len(words)}")

    occurences = words.count(word)
    print(f'Number of occurences of "{word}": {occurences}')
