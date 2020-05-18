class Solution:
    def isValid0(self, s: str) -> bool:
        while s:
            temp = s
            s = s.replace('()','')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            if temp == s:
                return False
        return True

    def isValid(self, s: str) -> bool:
        s = list(s)
        want = ('()','{}','[]')

        while s:
            temp = s.copy()
            if s[i]+s[i+1] in want:
                s.pop(i)
                s.pop(i)
                if temp == s:
                    return False

        return True

obj1 = Solution()
print(obj1.isValid('()[]'))