class Solution:
    def canArrange(self, arr, k: int) -> bool:
        for numberPosition in range(len(arr)):
            arr[numberPosition] = arr[numberPosition]%k
        arr.sort()
        zeroOccurrences = arr.count(0)
        startPointer = zeroOccurrences
        endPointer = len(arr)-1
        if zeroOccurrences%2:
            return False
        if (endPointer-startPointer+1) %2:
            return False
        while startPointer <= endPointer and arr:
            if arr[startPointer] + arr[endPointer] == k:
                startPointer +=1
                endPointer-=1
            else:
                return False
        return True
obj1 = Solution()
print(obj1.canArrange( arr = [-10,10], k = 2))

