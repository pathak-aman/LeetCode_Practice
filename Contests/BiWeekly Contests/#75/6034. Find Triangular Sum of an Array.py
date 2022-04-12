from typing import  List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while not len(nums) == 1:
            nums = [(nums[i+1] + nums[i]) % 10 for i in range(len(nums)-1)]
        return nums[0]

print(Solution().triangularSum([1,2,3,4,5]))
print(Solution().triangularSum([1]))
print(Solution().triangularSum([1100,1000]))