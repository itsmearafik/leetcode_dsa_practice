""" 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104 

"""

from typing import List


def searchInsert(nums: List[int], target_value: int ):
    # initializing pointers left and right  
    left = 0
    right = len(nums) - 1
    # binary search loop 
    while left <= right:
        # finding the midpoint_value (midean value)
        midpoint_value = (left + right) // 2

        # check if midpoint_value == target_value
        if nums[midpoint_value] == target_value:
            print(midpoint_value)
            return midpoint_value
        # move to the left side if midpoint_value is bigger than target_value
        elif nums[midpoint_value] >= target_value:
            right = midpoint_value - 1
        # move to the right side if midpoint_value is smaller than target_value
        else:
            left = midpoint_value + 1
    print(left)
    # print the target_value index if not found in list 
    return left


nums = [1,3,5,6]
# target_value = 

searchInsert(nums, target_value= 7)