# Find min and max element in a list
# Search an element within the list
# Find sum average of all elements of list

from ast import literal_eval as eval

nums = eval(input("Enter a list: "))
mini = maxi = nums[0]

for n in nums:
    if n < mini:
        mini = n
    if n > maxi:
        maxi = n
print(f"Minimum : {mini}, Maximum : {maxi}")

# search using linear search, which has complexity O(n)
to_search = int(input("Enter number to be searched: "))

searched = -1
searched = nums.index(to_search)
if searched >= 0:
    print(f"{to_search} found at position {searched}")
else:
    print(f"{to_search} not found")

average = 0
for n in nums:
    average += n
average /= len(nums)
print(f"Average : {average}")
