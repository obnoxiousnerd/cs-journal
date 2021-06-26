# Program to sort a list using bubble sort

nums = [23, 6, 8, 84, 16, 1, 75]
nums_sorted = nums.copy()
n = len(nums_sorted)

for i in range(n):
    for j in range(0, n - i - 1):
        if nums_sorted[j] > nums_sorted[j + 1]:
            nums_sorted[j], nums_sorted[j + 1] = nums_sorted[j + 1], nums_sorted[j]

print(nums_sorted)