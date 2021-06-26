# To print all even pairs from tuple pairs
from ast import literal_eval as eval

n = int(input("Enter number of tuple pairs: "))
all_tups = []

for i in range(n):
    print()
    tup = eval(input("Enter tuple pair: "))[:2]
    if tup[0] % 2 == 0 and tup[1] % 2 == 0:
        all_tups.append(tup)

print(tuple(all_tups))