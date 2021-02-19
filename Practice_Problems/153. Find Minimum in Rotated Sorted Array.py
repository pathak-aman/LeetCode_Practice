class Solution:
    def findMin(self, nums: list) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[start] < nums[mid]:
                start = mid+1
            else:
                end = mid-1
        return start
obj1 = Solution()
print(obj1.findMin([3,4,5,0,1,2]))




