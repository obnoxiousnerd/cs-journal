# Program to compute mean of mean of various tuples

import statistics
from ast import literal_eval as eval

n = int(input("Enter number of tuples: "))
means = []

for i in range(n):
    nums = eval(input("Enter the tuple: "))
    means.append(statistics.mean(nums))

tmean = statistics.mean(means)
print(f"Mean of means of tuples is {tmean}")