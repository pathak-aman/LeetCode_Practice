class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        freq_dict = {}
        for i in S:
            if freq_dict.get(i):
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        for j in J:
            count+=freq_dict.get(j,0)
        return count

obj1 = Solution()
print(obj1.numJewelsInStones(J = "aAb", S = "aAAbbbb"))
