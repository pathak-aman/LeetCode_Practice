class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):
            start, end = 0, len(s) - 1
            while start <= end:
                if s[start] != s[end]:
                    return False, start, end
                start += 1
                end -= 1
            return True, None, None

        palindrome, start, end = isPalindrome(s)
        if palindrome:
            return True
        else:
            if isPalindrome(s[start + 1: end+1])[0]:
                return True
            elif isPalindrome(s[start:end])[0]:
                return True
            else:
                return False

# print(Solution().validPalindrome("abc"))
print(Solution().validPalindrome("abcdgfgcba"))