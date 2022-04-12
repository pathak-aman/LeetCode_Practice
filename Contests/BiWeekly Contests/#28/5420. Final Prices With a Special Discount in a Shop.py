class Solution:
    def finalPrices(self, prices):
        output = []
        i = 0
        while i < len(prices):
            finalPrize = prices[i]
            j = i+1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    finalPrize = prices[i]-prices[j]
                    break
                j+=1
            i+=1
            output.extend([finalPrize])
        return output
obj1 = Solution()
print(obj1.finalPrices([8,10,20,6]))
