class Solution:
    def firstUniqChar(self, s: str) -> int:
        # i = 0
        # while i < len(s):
        #     if s.count(s[i]) == 1:
        #         return i
        #     i +=1
        # return -1
        #
        freq = dict()
        for i in s:
            if freq.get(i):
                freq[i] += 1
            else:
                freq[i] = 1
        print(freq)
        for key,value in freq.items():
            if value == 1:
                return s.find(key)
        return -1




obj1 = Solution()
print(obj1.firstUniqChar('aaaaaaaahfffffdh'))
