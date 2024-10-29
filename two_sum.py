# find two sums in an array that sum up to a given target value 

def twoSum( nums:list[int], target: int) -> list[int]:
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num 

        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i 


nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

print("______end of line______")

nums = [3,2,4]
target = 6

print(twoSum(nums, target))


"""
    Solution
1. Initialize a dictionary to store the numbers of the array and its indices (key:value pairs)
2. Loop through the array whiles calculating the complement of target on each number.
3. Check for complement in dictionary (it complement exists, return key:value)
4. Update dictionary (add key:value if complement is not in dictionary)
5. return key:value of complement  once found.
"""