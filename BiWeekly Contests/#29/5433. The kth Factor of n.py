class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        currentFactors = 1
        for number in range(2, n+1):
            if n%number == 0:
                currentFactors+=1
                if currentFactors == k:
                    return number
        return -1
obj1 = Solution()
print(obj1.kthFactor(n = 1000, k = 18))
