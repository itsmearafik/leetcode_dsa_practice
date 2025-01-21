'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

from typing import List


def singleNumber(nums: List[int]) -> int:
    # initialize var result= single value
    result = 0
    # iterate through arraychecking for non repeating values 
    for num in nums:
        result ^= num
    return result

print(singleNumber(nums=[2,2,1]))        