# DONE!
class Solution:
    def buildArray(self, target, n: int):
        initialValue = 1
        output = []
        for number in target:
            multiplier = number - initialValue
            output.extend(["Push","Pop"]*multiplier + ["Push"])
            initialValue = number + 1
        return output
obj1 = Solution()
print(obj1.buildArray([10,13,20], n = 40))
