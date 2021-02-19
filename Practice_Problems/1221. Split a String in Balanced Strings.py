class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balancedFactor = 0
        splitCount = 0
        for letter in s:
            if letter == 'R':
                balancedFactor -= 1
            else:
                balancedFactor += 1
            if not balancedFactor:
                splitCount+=1
        return splitCount

obj1 = Solution()
print(obj1.balancedStringSplit('LRLRLLLRLLR'))
