class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    def lengthOfLongestSubstring(self, s):
        if s == '':
            return 0 
        max_length = 1
        while True:
            flag = False
            for i in range(len(s)-max_length):
                if len(set(s[i:i+max_length+1])) == max_length+1:
                    flag = True
                    break
            if flag:
                max_length +=1
            else:
                break
        return max_length

obj1 = Solution()
print(obj1.lengthOfLongestSubstring('abcabcdb'))
