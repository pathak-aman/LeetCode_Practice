class Solution:
    def reverseString(self, s):
        startIndex = 0
        endIndex = len(s)-1
        while startIndex <=endIndex:
            s[startIndex],s[endIndex] = s[endIndex],s[startIndex]
            startIndex+=1
            endIndex-=1
        return s
obj1 = Solution()
print(obj1.reverseString(["q","t"]))
