class Solution:
    def decompressRLElist(self, nums: list) -> list:
        output = []
        start = 0
        while start < len(nums)//2:
            output.extend(nums[(2*start)]*[nums[2*start+1]])
            start+=1
        return output
obj1 = Solution()
print(obj1.decompressRLElist([1,2,3,4]))

