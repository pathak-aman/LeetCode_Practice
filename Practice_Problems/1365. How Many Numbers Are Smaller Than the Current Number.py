from sortedcontainers import SortedDict

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        occurenceDictionary = dict()
        for num in nums:
            if occurenceDictionary.get(num):
                occurenceDictionary[num]+=1
            else:
                occurenceDictionary[num]=1
        sortedOccurenceDictionary = SortedDict(occurenceDictionary)
        minimalOccurenceKey = sortedOccurenceDictionary.popitem(index = 0)
        prevTemp = minimalOccurenceKey[1]
        for key, value in sortedOccurenceDictionary.items():
            currTemp = value
            sortedOccurenceDictionary[key] = prevTemp
            prevTemp = prevTemp+currTemp
        sortedOccurenceDictionary[minimalOccurenceKey[0]] = 0
        # for pos in range(len(nums)):
        #     nums[pos] = sortedOccurenceDictionary[nums[pos]]
        return [sortedOccurenceDictionary[i] for i in nums]

obj1 = Solution()
print(obj1.smallerNumbersThanCurrent([0,0,0,0,1,1,1,1,11,6,5,4,8]))

