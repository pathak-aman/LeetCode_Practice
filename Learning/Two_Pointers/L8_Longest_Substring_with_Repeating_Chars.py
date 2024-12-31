class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        max_length = 0
        map = {}
        while r < len(s):
            # Add
            map[s[r]] = map.get(s[r],0) + 1
            print(map, s[l:r+1])

            # Invalidity:
            if len(map) > 2 or min(map.values()) > k:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    map.pop(s[l])
                l += 1
            
            # Validity:
            if len(map) <= 2 and min(map.values()) <= k:
                max_length = max(max_length, r - l + 1)

            r += 1
        return max_length
s = "AVAVAAAEFAAABABBA"
k = 4
print(Solution().characterReplacement(s, k))