# DONE!
class Solution:
    def stringMatching(self, words):
        answer = set()
        for i in words:
            for j in words:
                if i in j and i!=j:
                    answer.add(i)
        return list(answer)

obj1 = Solution()
print(obj1.stringMatching(words = ["a",'oplkm',
                          'm',"as","aas",'ma','aman']))
