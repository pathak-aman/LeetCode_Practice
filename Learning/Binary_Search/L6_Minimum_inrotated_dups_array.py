from math import inf

class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        min_num = inf
        while l <= r:
            mid = (l+r) // 2

            # Sorted section, directly check arr[l]
            if nums[l] < nums[mid] < nums[r]:
                min_num = min(min_num, nums[l])
                break
                
            elif nums[l] == nums[mid] == nums[r]:
                min_num = min(min_num, nums[l])
                l += 1
                r -= 1
                continue

            # Identify the sorted half
            # Elimiate it but check the min before moving l, r pointers

            if nums[l] <= nums[mid]:
                min_num = min(min_num, nums[l])
                l = mid + 1
            elif nums[mid] <= nums[r]:
                min_num = min(min_num, nums[mid])
                r = mid - 1

        return min_num
    
if __name__ == "__main__":

    arrays = [
        [3,3,3,3,3,6,0,1,2,3,3,3,3,3,3],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,1,2,3,3,3,3,3,3],
        [4,5,1,2,3],
        [-100,-100,-100,-100,-100,6,6,6,10,10,78,78,78,100, 100,100,100,-200,-100,-100,-100,-100,-100,-100],
        [36,36,36,100,2000,2000,2000,2000,8999,-99999, -90, -9, 0]

    ]

    for array in arrays:
        print(array, Solution().findMin(array))



#  l     m l   l,r m              r
# [3,3,3,3,3,6,0,1,2,3,3,3,3,3,3], 1