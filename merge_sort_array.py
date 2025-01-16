from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        midx = m - 1
        nidx = n - 1
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
        else:
            nums1[right] = nums2[nidx]
            nidx -= 1
            
        right -= 1
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
print(merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
