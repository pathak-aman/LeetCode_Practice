# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
'''j'''


# class Solution:
#     # def twoSum(self, nums: list[int], target: int) -> List[int]:
#     def twoSum(self,nums,target):
#         num_occurrence = set(nums)
#         for i in num_occurrence:
#             if target - i in num_occurrence:
#                 d = nums.index(i)
#                 nums.remove(i)
#                 print(nums)
#                 nums.insert(d,target+1)
#                 print(nums)
#                 e = nums.index(target - i)
#                 return [d,e]
#
# instance = Solution()
# nums = [0,4,3,0]
# target = 0
# print(instance.twoSum(nums,target))


class Solution:
    def twoSum(self, nums, target):
        sorted_nums = sorted(nums)
        front = 0
        rear = len(nums) - 1

        while front <= rear:
            sums = sorted_nums[front] + sorted_nums[rear]
            if sums == target:
                front = sorted_nums[front]
                rear = sorted_nums[rear]
                d1 = nums.index(front)
                nums.remove(front)
                # nums.insert(d1, target + 1)
                d2 = nums.index(rear)
                return [d1, d2 + 1]
            elif sums < target:
                front += 1
            else:
                rear -= 1


instance = Solution()
nums = [0, 4, 0, 3]
target = 0
print(instance.twoSum(nums, target))
