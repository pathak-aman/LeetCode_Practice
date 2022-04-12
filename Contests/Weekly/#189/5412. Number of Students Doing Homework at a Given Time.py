class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        students = 0
        for start,end in zip(startTime,endTime):
            if start<=queryTime<=end:
                students += 1
        return students

obj1 = Solution()
print(obj1.busyStudent([9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
