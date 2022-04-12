class Solution:
    def isPalindrome(self, s: str) -> bool:
        for letter in set(s):
            if not letter.isalnum():
                s = s.replace(letter,'')
        s = s.lower()
        return s == s[::-1]
obj1 = Solution()
print(obj1.isPalindrome("aabb"))
