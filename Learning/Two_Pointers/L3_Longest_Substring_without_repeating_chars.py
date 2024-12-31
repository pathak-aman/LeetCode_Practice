class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_map = {}

        l, r = 0,0 
        max_length = 0 

        while r < len(s):
            if s[r] in dict_map:
                # Yes, occured already
                if dict_map[s[r]] >= l:
                    l = dict_map[s[r]] + 1

            dict_map[s[r]] = r
            # max_length = max(max_length, r - l + 1)
            if r - l + 1 > max_length:
                max_length = r - l + 1
                best_l = l
                best_r = r
            r += 1
        print(s[best_l:best_r+1])
        return max_length


s = "amanpathak"
print(Solution().lengthOfLongestSubstring(s))