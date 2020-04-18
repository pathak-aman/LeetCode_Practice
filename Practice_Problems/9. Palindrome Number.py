#DONE!
class Solution:
    def isPalindrome0(self, x: int) -> bool:
        if x < 0:
            return False
        digits = []
        temp = x
        while x!=0:
            d = x%10
            x //=10
            digits.append(d)
        print(digits)

        start = 0
        end = len(digits)-1
        while start <= end:
            if not digits[start] == digits[end]:
                return False
            start +=1
            end -=1
        return True

    def isPalindrome1(self, x: int) -> bool:
        x_str = str(x)
        start = 0
        end = len(x_str)-1
        while start <=end:
            if not x_str[start] == x_str[end]:
                return False
            start += 1
            end -= 1
        return True

    def isPalindrome2(self, x: int) -> bool:
        x_str = str(x)
        if x_str == x_str[::-1]:
            return True
        else:
            return False

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num*10+x%10
            x //=10
        return x == rev_num or x == rev_num // 10

obj1 = Solution()
num = 91232191
print(obj1.isPalindrome(num))
