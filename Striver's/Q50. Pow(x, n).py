# Q50. Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if abs(n) >= 2:
            multiple = n // 2
            remainder = n % 2
            if remainder:
                return self.myPow(x * x, multiple) * x * remainder
            else:
                return self.myPow(x * x, multiple)
        else:
            if n < 0:
                return 1/x
            else:
                return x


obj = Solution()
x = 6
pow = 1
print(obj.myPow(x,pow))
print(obj.myPow(-x,pow))
print(obj.myPow(x,-pow))
print(obj.myPow(-x,-pow))
