class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True
obj1 = Solution()
print(obj1.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
