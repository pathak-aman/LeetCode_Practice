class Solution:
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [0] * size
        prod = 1
        for i in range(size):
            prod *= nums[i]
            nums[i] = nums[i] ** -1
        for i in range(size):
            output[i] = int(prod * nums[i])
        return output


obj1 = Solution()
print(obj1.productExceptSelf([1,2,3,4,0]))



