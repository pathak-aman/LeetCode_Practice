class Solution:
    def runningSum(self, nums):
        output = []
        sum = 0
        for number in nums:
            sum += number
            output.extend([sum])
        return output
obj = Solution()
print(obj.runningSum([]))
