class Solution:
    def kLengthApart(self, nums, k) -> bool:
        # if nums.count(1) < 2 or k ==0:
        #     return True
        # else:
        #     _ = [i for i in range(len(nums)) if nums[i]==1]
        #     for i in range(len(_)-1):
        #         if not _[i+1] -_[i] >k:
        #             return False
        #     return True
        if k == 0: return True

        ones, zeros = nums.count(1), nums.count(0)

        distance = (ones - 1) * k

        if distance <= zeros:
            return True
        else:
            return False
obj1 = Solution()
print(obj1.kLengthApart([1,0,1,0,0,0,1,0,1,1,0,0,0],2))
