class Solution:
    def peopleIndexes(self, favoriteCompanies):
        output = []
        i = 0
        while i < len(favoriteCompanies):
            j = 0
            answer = True
            while j < len(favoriteCompanies):
                if i!=j and set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])):
                    answer = False
                    break
                j+=1
            if answer:
                output.append(i)
            i+=1
        return output

obj1 = Solution()
print(obj1.peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
