class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        zipped_pairs = zip(indices, list(s))
        return ''.join([x for _, x in sorted(zipped_pairs)])
obj1 = Solution()
print(obj1.restoreString(s = "aiohn", indices = [3,1,4,2,0]))
