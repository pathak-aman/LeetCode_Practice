class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        return [i+extraCandies >=max_candy for i in candies]

obj1=Solution()
candies = [4,2,1,1,2]
c = 2
obj1.kidsWithCandies(candies,c)


