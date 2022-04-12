from math import factorial
class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        if len(nums) == len(set(nums)):
            return 0
        output = 0
        occurenceDict = {}
        fact = factorial
        for number in nums:
            if occurenceDict.get(number):
                occurenceDict[number] +=1
            else:
                occurenceDict[number] = 1
        for occurences in occurenceDict.values():
            if occurences > 1:
                output+= fact(occurences)/2/fact(occurences - 2)
        return int(output)
obj1 = Solution()
print(obj1.numIdenticalPairs(nums = [1,2,3,4,5]))

