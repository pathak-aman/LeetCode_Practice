class Solution:
    def maxProduct(self, nums:list) -> int:
        firstNumber = max(nums)
        nums.remove(firstNumber)
        secondNumber = max(nums)
        return (firstNumber-1)*(secondNumber-1)
obj1 = Solution()
print(obj1.maxProduct(nums = [3,7]))
