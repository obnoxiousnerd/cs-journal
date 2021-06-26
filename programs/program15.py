# Input two tuples and merge them in order
# First tuple elements are followed by second tuple elements

from ast import literal_eval as eval

t1 = eval(input("Enter the first tuple: "))
t2 = eval(input("Enter the second tuple: "))

t3_len = len(t1) + len(t2)
t3 = list()

for i in range(t3_len):
    if len(t1) > i:
        t3.append(t1[i])
    if len(t2) > i:
        t3.append(t2[i])

print(tuple(t3))