class Solution:
    # def numSub(self, s: str) -> int:
    #     totalSubstring = 0
    #     countStart = False
    #     lengthSubstring = 0
    #     occurenceDict = {}
    #
    #     for letter in s:
    #         if countStart:
    #             if letter == '1':
    #                 lengthSubstring+=1
    #             else:
    #                 if occurenceDict.get(lengthSubstring):
    #                     occurenceDict[lengthSubstring]+=1
    #                 else:
    #                     occurenceDict[lengthSubstring] = 1
    #                 lengthSubstring = 0
    #                 countStart = False
    #         else:
    #             if letter == '1':
    #                 countStart = True
    #                 lengthSubstring = 1
    #
    #     if countStart and lengthSubstring:
    #         if occurenceDict.get(lengthSubstring):
    #             occurenceDict[lengthSubstring] += 1
    #         else:
    #             occurenceDict[lengthSubstring] = 1
    #
    #     for key,values in occurenceDict.items():
    #         totalSubstring += (values*key*(key+1)//2)
    #
    #     return totalSubstring % (10**9+7)
    def numSub(self, s: str) -> int:
        countStart = True
        totalSubstring = 0
        lengthSubstring = 0

        for letter in s:
            if countStart:
                if letter == '1':
                    lengthSubstring+=1
                else:
                    totalSubstring+=lengthSubstring*(lengthSubstring+1)//2
                    countStart = False
            else:
                if letter == '1':
                    countStart = True
                    lengthSubstring = 1
        if countStart and lengthSubstring:
            totalSubstring += lengthSubstring * (lengthSubstring + 1) // 2
        return totalSubstring % (10**9+7)

obj1 = Solution()
print(obj1.numSub('11011011010001'))
