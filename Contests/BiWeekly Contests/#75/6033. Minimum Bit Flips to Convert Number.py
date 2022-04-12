class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin, goal_bin = bin(start)[2:], bin(goal)[2:]
        if goal >= start:
            big = goal_bin
        else:
            big = start_bin
        extra_ones = big[0:abs(len(start_bin) - len(goal_bin))].count("1")
        return sum([1 for i,j in zip(start_bin[::-1],goal_bin[::-1]) if i != j]) + extra_ones


print((Solution().minBitFlips(10,82)))
print((Solution().minBitFlips(0,82)))