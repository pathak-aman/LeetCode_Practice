class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        leftRight = {'(': ')', '{': '}', '[': ']'}
        for bracket in s:
            if bracket in leftRight:
                stack.append(bracket)
            else:
                if not (stack and leftRight[stack.pop()]) == bracket:
                    return False
        return len(stack) == 0
    # def isValid(self, s: str) -> bool:
    #     s = list(s)
    #     want = ('()','{}','[]')
    #
    #     while s:
    #         temp = s.copy()
    #         if s[i]+s[i+1] in want:
    #             s.pop(i)
    #             s.pop(i)
    #             if temp == s:
    #                 return False
    #
    #     return True
obj1 = Solution()
print(obj1.isValid0('()[{()[]}]'))