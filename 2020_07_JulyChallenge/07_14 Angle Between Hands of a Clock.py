class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        minuteAngle = 6*minutes
        hourAngle = 30*hour + 0.5*minutes
        print (hourAngle,minuteAngle)
        return abs(hourAngle-minuteAngle)
obj1 = Solution()
print(obj1.angleClock(hour = 0, minutes = 30))
