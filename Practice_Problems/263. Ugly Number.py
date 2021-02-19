class Solution:
    def isUgly(self, num: int) -> bool:
        while num >1:
            if num % 2 == 0:
                num = num//2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            else:
                return False
        return True
obj1 = Solution()
print(obj1.isUgly(68))
