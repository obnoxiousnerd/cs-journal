# Program to search using binary search.


def binary_search(arr, key):
    """
    Function binary_search returns the zero-based index of the
    found number in the given array.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


nums = [5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
num = int(input("Enter the number to search: "))

index = binary_search(nums, num)

if index < 0:
    print(f"Number {num} not found")
else:
    print(f"Number {num} found at index {index}")
