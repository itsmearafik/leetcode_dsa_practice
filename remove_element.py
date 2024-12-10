""" 
Problem: Given an integer array `nums` and integer `val`, 
        remove all occurences of `val` in `nums` in-place,
        Then return the number of elements in `nums` which are not equal to `val`.
        Consider the number of elements in `nums` which are not equal to `val` be `k`, to
        get accepted, you need to do the following things: 
        -> change the array `nums` such that the first `k` elements of `nums` contain the elements
        which are not equal to `val` The remaining elements and size of `nums` are not important.
        -> return `k`.
        Constraints: 0 <= nums.length <= 100, 0 <= nums[i] <= 50, 0 <= val <= 100 
"""

# 1. Intialize `k` to 0
# use a loop to iterate through `nums`  using the index: bcos u dont kow the size
# inside the loop use a condition to check for `val` 
# if element is not equal to val, assign/append to `k` list and increment by 1
# return `k` list after completing loop 

# This method is linear because it loops through all the elements in the list (time complexity O(n) and will return the elements in a new list `k` which is also linear (space complexity O(n) hence O(n x n))

def removeElement(nums, val):
    """ 
    :type nums: List[int]
    :type val: int
    :rtype k: int
    """
    k = 0
    for i in range(len(nums)):
        if (nums[i] != val):
            nums[k] = nums[i]
            k += 1
    return k 


print(removeElement([3,2,2,3], 3))