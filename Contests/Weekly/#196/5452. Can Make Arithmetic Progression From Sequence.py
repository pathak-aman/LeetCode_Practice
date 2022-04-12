class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        commonDifference= arr[1]-arr[0]
        for nums in range(1,len(arr)-1):
            if not arr[nums+1] - arr[nums] == commonDifference:
                return False
        return True
obj1= Solution()
print(obj1.canMakeArithmeticProgression([1,5,3]))
