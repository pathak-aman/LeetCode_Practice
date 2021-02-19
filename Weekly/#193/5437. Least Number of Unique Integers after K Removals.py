class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        occurrenceDictionary = dict()
        for number in arr:
            if occurrenceDictionary.get(number):
                occurrenceDictionary[number]+=1
            else:
                occurrenceDictionary[number]=1
        occurrenceValuesList = sorted(list(occurrenceDictionary.values()))
        numberUniqueIntergers = len(occurrenceValuesList)
        if not k:
            return numberUniqueIntergers
        sum = 0
        for value in occurrenceValuesList:
            sum+=value
            if sum <= k:
                numberUniqueIntergers-=1
            else:
                break
        return numberUniqueIntergers

obj1 = Solution()
print(obj1.findLeastNumOfUniqueInts( arr = [1], k = 1))

