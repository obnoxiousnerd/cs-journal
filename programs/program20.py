# Count frequency of list element using dictionary

from ast import literal_eval as eval

frequencies = {}
things = eval(input("Enter a list: "))
for thing in things:
    if thing in frequencies.keys():
        count = frequencies[thing]
    else:
        count = 0
    frequencies[thing] = count + 1
print(frequencies)