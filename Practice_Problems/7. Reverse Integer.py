class Solution:
    def reverse(self, x: int):
        # if x > 0:
        #     x = int(str(x)[::-1])
        # else:
        #     x = int('-'+(str(x)[1:])[::-1])
        #
        # if -2**31 <= x <=2**31-1:
        #     return x
        # else:
        #     return 0

        neg = False
        if x < 0:
            neg = True
            x *= -1
        rev_number = 0
        while x > 0:
            rev_number = rev_number * 10 + x % 10
            x //= 10
        if neg:
            rev_number *= -1
        if -2147483648 <= rev_number <= 2147483647:
            return rev_number
        else:
            return 0


a = -123
obj1 = Solution()
print(obj1.reverse(a))
