# Program to sort a list using insertion sort

nums = [23, 6, 8, 84, 16, 1, 75]
nums_sorted = nums.copy()
n = len(nums_sorted)

for i in range(1, len(nums_sorted)):

    key = nums_sorted[i]

    j = i - 1
    while j >= 0 and key < nums_sorted[j]:
        nums_sorted[j + 1] = nums_sorted[j]
        j -= 1
    nums_sorted[j + 1] = key

print(nums_sorted)