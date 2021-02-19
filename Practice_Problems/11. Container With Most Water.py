class Solution:
    def maxArea(self, height) -> int:
        start,end = 0,len(height)-1
        currentWater = 0
        maxWater = 0
        while start < end:
            containerHeight = min(height[start], height[end])
            currentWater = containerHeight*(end-start)
            if currentWater > maxWater:
                maxWater = currentWater
            if containerHeight == height[start]:
                start+=1
            else:
                end-=1
        return maxWater
obj1 = Solution()
print(obj1.maxArea([7,3,4,8,2,5,67,22,9]))
