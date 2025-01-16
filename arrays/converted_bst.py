# Definition for a binary tree node.
from typing import List, Optional



def TreeNode(val=0, left=None, right=None):
    val = val
    left = left
    right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    total_nums = len(nums)
    if not total_nums: 
        return None

    mid_node = total_nums // 2
    return TreeNode(
        nums[mid_node],
        sortedArrayToBST(nums[:mid_node]), sortedArrayToBST(nums[mid_node + 1 :])
    )
    print(sortedArrayToBST)


nums = [0, 1, 2, 3, 4, 5, 6, 7]
sortedArrayToBST(nums)
