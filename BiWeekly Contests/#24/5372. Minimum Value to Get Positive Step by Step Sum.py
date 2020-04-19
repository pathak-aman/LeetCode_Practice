class Solution:
    def minStartValue(self, nums):
        d,startvalue =  1,1
        for i in nums:
            d+=i
            if d<1:
                startvalue += -d+1
                d=1
        return startvalue

obj1=Solution()
print(obj1.minStartValue([-3,-3,-3,4,10,-20,30]))
