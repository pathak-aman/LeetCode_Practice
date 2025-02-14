# Problem is asking that involves continuous finding the max/min elements
# Max/Min is continuously removed

import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operations = 0
        while nums[0] < k:
            x,y = heapq.heappop(nums), heapq.heappop(nums)
            z = 2 * x + y
            heapq.heappush(nums, z)
            operations += 1
        return operations