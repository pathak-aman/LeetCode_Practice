# Done!

"""Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""

class Solution:
    def maxSubArray(self, nums):
        sum = True
        for i in nums:
            if i > 0:
                sum = False
                break
        if sum:
            return max(nums)

        max_sum = 0
        current_sum = 0
        # index = -1
        for i in range(len(nums)):
            current_sum += nums[i]
            if current_sum < 0:
                current_sum = 0
            if current_sum > max_sum:
                # index = i
                max_sum = current_sum
        return max_sum


        # print(nums)
        # print(max_sum,index)
        # print(nums[index::-1])
        # sum = 0
        # for i in range(index,-1,-1):
        #     sum += nums[i]
        #     if sum == max_sum:
        #         sum = i
        #         # print(sum)
        #         # print(nums[:i])
        #         break

obj1 = Solution()
a = [-2,-2,-2,1]
print(obj1.maxSubArray(a))