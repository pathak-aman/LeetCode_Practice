class Solution:
    # def search1(self, nums:list  ,target):
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         return -1
    def search(self, nums:list  ,target):
        st = 0
        end = nums.__len__()-1
        while st<=end:
            mid = (st+end)//2
            if nums[mid] == target:
                return mid
            elif nums[st]<=target<nums[mid]:
                end = mid-1
            else:
                st = mid+1
        return -1

obj1 = Solution()
print(obj1.search([5,1,3],2))
