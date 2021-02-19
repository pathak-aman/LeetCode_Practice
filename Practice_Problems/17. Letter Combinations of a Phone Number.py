from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list:
        if not len(digits):
            return []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['grid', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        result = []
        listsForCartesianProduct = []
        for i in digits:
            listsForCartesianProduct.append(phone[i])
        for combination in product(*listsForCartesianProduct):
            result.append("".join(combination))
        return result

print(Solution().letterCombinations("789"))