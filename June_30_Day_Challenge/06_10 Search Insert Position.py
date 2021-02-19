class Solution:
    def searchInsert(self, nums, target: int) -> int:
        start, end = 0,len(nums)-1
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid+1
            else:
                end = mid-1
        return start
obj1 = Solution()
print(obj1.searchInsert([],10009))

