from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1+sqrt(1+8*n))/2)

obj = Solution()
print(obj.arrangeCoins(n=21))

