class Solution:
    def threeSum(self, nums: list):
        nums.sort()
        positiveIndex = -1
        isZero = False
        for number in nums:
            if number>=0:
                if number == 0:
                    isZero = True
                positiveIndex = nums.index(number)
                break

        if positiveIndex == 0 or positiveIndex == -1:
            return []

        startPointer  = 0
        endPointer = len(nums)-1
        thirdPointer = 0
        outputList = []

        while startPointer<=endPointer:

            difference = nums[endPointer] - nums[startPointer]
            if difference == 0 and isZero:
                outputList.append([nums[startPointer],0,nums[endPointer]])
            elif difference > 0:
                while startPointer <= positiveIndex:
                    difference = nums[endPointer] - nums[startPointer]
                    if self.BinarySearch(nums[startPointer+1:positiveIndex],difference):
                        outputList.append([nums[startPointer], difference, nums[endPointer]])
                    startPointer = startPointer+1
            else:
                if self.BinarySearch(nums[positiveIndex:endPointer+1],difference):
                    outputList.append([nums[startPointer], difference, nums[endPointer]])

    def BinarySearch(self,nums:list,target:int):
        leftPointer = 0
        rightPointer = len(nums)-1
        while leftPointer <= rightPointer:
            midPointer = (leftPointer+rightPointer)//2
            if target == nums[midPointer]:
                return True
            elif target < nums[midPointer]:
                rightPointer = midPointer-1
            else:
                leftPointer = midPointer+1
        return False
obj1 = Solution()
print(obj1.BinarySearch([-2,-1,0,4,5,6,7,8,9],0))

