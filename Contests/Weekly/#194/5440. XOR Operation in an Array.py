class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arrayofTwos = [start + 2*i for i in range(n)]
        xor = 0
        for num in arrayofTwos:
            xor^=num
        return xor

obj1 = Solution()
print(obj1.xorOperation(n = 5, start = 4))

