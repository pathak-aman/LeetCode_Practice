# Use the approach: "for i" , instead of considering the substrings begininning with arr[i], we'll take substring that end with arr[i]

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        char_map = [-1] * 3
        for i in range(len(s)):
            char_map[ord(s[i]) - ord('a')] = i

            if min(char_map) != -1:
                count += min(char_map) + 1
        return count

s = "bbacba"
print(Solution().numberOfSubstrings(s))
