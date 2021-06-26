# To perform left shift, right shift on a list and
# reverse it

from ast import literal_eval as eval

nums = eval(input("Enter a list: "))
nums_length = len(nums)

right = nums.copy()
right[0] = nums[nums_length - 1]
right[1:nums_length] = nums[: nums_length - 1]

left = nums.copy()
left[:nums_length] = nums[1:nums_length]
left.append(nums[0])

reverse = nums.copy()
for i in range(nums_length):
    reverse[nums_length - 1 - i] = nums[i]

print(f"Left shift: {left}")
print(f"Right shift: {right}")
print(f"Reversed: {reverse}")