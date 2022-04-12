# Q31. Next Permutation

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return

        pos = n - 2
        while pos >= 0 and nums[pos] >= nums[pos + 1]:
            pos -= 1

        # Skips for cases that are decreasing
        if pos >= 0:
            big = n - 1
            while nums[pos] >= nums[big]:
                big -= 1
            nums[pos], nums[big] = nums[big], nums[pos]

        nums[pos+1:] = nums[-1:pos-n:-1]
        return nums

obj = Solution()
print(obj.nextPermutation([2,7,8]))