class Solution:
    def kLengthApart(self, nums, k) -> bool:
        if nums.count(1) < 2:
            return True
        else:
            _ = [i for i in range(len(nums)) if nums[i]==1]
            for i in range(len(_)-1):
                if not _[i+1] -_[i] >k:
                    return False
            return True
obj1 = Solution()
print(obj1.kLengthApart([1,0,1,0,0,0,1,0,1,1,0,0,0],1))
