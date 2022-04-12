# Done

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max_profit = 0
        current_profit = 0

        for price in prices[1:]:
            if price > sell:
                sell = price
                current_profit = sell - buy
                if current_profit > max_profit:
                    max_profit = current_profit

            elif buy > price:
                buy = price
                sell = price
                current_profit = 0

        return max_profit