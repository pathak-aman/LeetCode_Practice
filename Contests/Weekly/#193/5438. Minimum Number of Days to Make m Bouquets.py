import operator


class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:
        if m == 1 and k ==1:
            return min(bloomDay)
        if len(bloomDay) < m*k:
            return -1

        high = []
        for bouquets in range(m):
            minHigh = 10 ** 9
            left,right = 0,k-1
            while left < len(bloomDay) and right <len(bloomDay):
                highestIndex,currentHigh = max(enumerate(bloomDay[left:right+1]), key=operator.itemgetter(1))
                highestIndex = left+highestIndex
                if currentHigh < minHigh:
                    minHigh = currentHigh
                    start = left
                    end = right
                left = highestIndex+1
                right = left +k -1
            bloomDay = bloomDay[:start] + bloomDay[end+1:]
            high.extend([minHigh])
        return max(high)
obj1 = Solution()
print(obj1.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))

