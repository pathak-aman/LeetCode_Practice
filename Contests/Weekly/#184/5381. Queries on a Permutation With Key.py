# DONE!
class Solution:
    def processQueries(self, queries, m):
        answer = []
        p = [i for i in range(1,m+1)]
        for q in queries:
            d = p.index(q)
            answer.extend([d])
            p = [p[d]] + p[0:d] + p[d+1:]
        return answer

obj1 = Solution()
print(obj1.processQueries([2,3,4,1,1,2,3],6))