class Solution:
    def avoidFlood(self, rains):
        # return condition:
        occurrenceDictionary = dict()
        for rain in rains:
            if occurrenceDictionary.get(rain):
                occurrenceDictionary[rain]+=1
            else:
                occurrenceDictionary[rain]=1
        zerosOccurance = occurrenceDictionary.get(0,0)
        if zerosOccurance:
            occurrenceDictionary.pop(0)
        multipleOccurances = 0
        for occurance in occurrenceDictionary.values():
            if occurance > 1:
                multipleOccurances+=1
        if multipleOccurances > zerosOccurance:
            return []
        if multipleOccurances == 0 and zerosOccurance == 0:
            return [-1]*len(rains)

        dryLakes = set(rains)-{0}
        fullLakes = set()
        output = []
        for rain in rains:
            if rain == 0:
                if len(fullLakes):
                    poppedLake = fullLakes.pop()
                    dryLakes.add(poppedLake)
                    output.extend([poppedLake])
                else:
                    output.extend([1])
            elif rain in dryLakes:
                dryLakes.remove(rain)
                fullLakes.add(rain)
                output.extend([-1])
            elif rain in fullLakes:
                return []
            print(dryLakes,fullLakes)
        return output
obj1 = Solution()
print(obj1.avoidFlood(rains = [1,2,0,2,3,0,1]))
