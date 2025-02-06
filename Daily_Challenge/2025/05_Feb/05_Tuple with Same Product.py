# Number of total pairs (a,b,c,d) = 2 * pairs * 2 * (pairs-1)

from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        product_dict = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_dict[product] += 1

        for value in product_dict.values():
            ans += 4 * value * (value - 1)

        return ans
