"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
# Solution 1

# class Solution:
#     def moveZeroes(self, nums) :
#         zeroes = [i for i in range(len(nums)) if nums[i] == 0]
#         print(zeroes)
#         #[0, 1, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
#         zeroes.reverse()
#         for i in zeroes:
#             nums.pop(i)
#         nums.extend([0]*len(zeroes))

# Solution 2

class Solution:
    def moveZeroes(self, nums) :
        count = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                while j <= len(nums)-2:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    j +=1
                    print(nums)


a = [0,0,1,0,3,5,3,1,45,0,0,6,3,6]
obj1 = Solution()
obj1.moveZeroes(a)
