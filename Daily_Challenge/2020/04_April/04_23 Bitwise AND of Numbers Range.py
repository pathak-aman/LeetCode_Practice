class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while (m != n):
            m >>= 1
            n >>= 1
            i += 1
        return n << i
obj1 = Solution()
print(obj1.rangeBitwiseAnd(34,20000000))