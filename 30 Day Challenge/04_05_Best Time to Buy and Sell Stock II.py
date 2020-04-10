# Done!
class Solution:
    def maxProfit(self, prices):
        # return sum([prices[i+1]-prices[i] for i in range(len(prices)-1) if prices[i+1]-prices[i] > 0])
        profit = 0
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            if diff > 0:
                profit+=diff
        return profit

obj1 = Solution()
print(obj1.maxProfit([7,1,2,5,3,6]))