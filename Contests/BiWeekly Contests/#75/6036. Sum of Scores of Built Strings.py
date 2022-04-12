class Solution:
    def sumScores(self, s: str) -> int:
        final_score = len(s)
        for i in range(1, len(s)):
            print(s[:i], s[-i:])
            if s[:i].(s[-i:]):
                print("INSIDE")
                final_score += sum([1 for a,b in zip(s[:i],s[-i:]) if a == b])
        return final_score
print(Solution().sumScores("azbazbzaz"))