from typing import List


# Search in sorted half
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                # 1st Half is sorted
                if nums[low] <= target <= nums[mid]:
                    # In 1st half
                    high = mid - 1
                else:
                    # In 2nd half
                    low = mid + 1
            else:
                # 2nd Half is sorted
                if nums[mid] <= target <= nums[high]:
                    # In 2nd half
                    low = mid + 1
                else:
                    # In 1st half
                    high = mid - 1
        return -1


# nums = [4, 5, 6, 7, 0, 1, 2, 3]
# nums = [12, 15, 18, 20, 23, 26, 29, 32, 38, 56, 67, 89, 0, 1, 4, 6, 7, 8, 10, 11]
# nums = [3,1]
nums = [4,5,5,5,5,6,6,7,0,0,0,0,1,1,1,1,2,2,2,2,3,4]
for i in nums:
    print(i, Solution().search(nums=nums, target=i+1))
