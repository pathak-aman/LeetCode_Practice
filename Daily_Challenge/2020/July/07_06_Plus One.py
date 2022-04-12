class Solution:
    def plusOne(self, digits: list) -> list:
        totalDigits = len(digits)
        if digits[totalDigits-1] < 9:
            digits[totalDigits-1] = digits[totalDigits-1] +1
            return digits
        else:
            for digitPositionReverse in range(totalDigits-1,-1,-1):
                print(digitPositionReverse)
                if digits[digitPositionReverse] == 9:
                    digits[digitPositionReverse] = 0
                else:
                    digits[digitPositionReverse] = digits[digitPositionReverse] + 1
                    return digits
            digits = [1]+digits[:]
            return digits
obj1 = Solution()
print(obj1.plusOne([9,9,9,9,9,9,9]))
