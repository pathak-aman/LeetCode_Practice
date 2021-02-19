class Solution:
    def rangeSum(self, nums: list, n: int, left: int, right: int) -> int:
        outputArray = nums.copy()
        for windowSize in range(2,n+1):
            for pos in range(n-windowSize+1):
                outputArray.append(sum(nums[pos:pos+windowSize]))
        outputArray.sort()
        return sum(outputArray[left-1:right])
obj1 = Solution()
print(obj1.rangeSum(nums = [1,2,3,4], n = 4, left = 3, right = 4))
