# Stupid LeetCode!
class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        import numpy as np
        return np.median(sorted(nums1+nums2))

instance = Solution()
num1 = [3,4,7,3,5]
num2 = [2,4]
print(instance.findMedianSortedArrays(num1,num2))