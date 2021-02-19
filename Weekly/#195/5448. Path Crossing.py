class Solution:
    def isPathCrossing(self, path: str) -> bool:
        xCoordinate = 0
        yCoordinate = 0
        pointsCovered = [(0,0)]
        for direction in path:
            if direction == 'N':
                yCoordinate+=1
            elif direction == 'S':
                yCoordinate-=1
            elif direction == 'E':
                xCoordinate +=1
            else:
                xCoordinate-=1
            pointsCovered.append((xCoordinate,yCoordinate))
        return not len(pointsCovered) == len(set(pointsCovered))
obj1 = Solution()
print(obj1.isPathCrossing(path = "NESEEESSSNNNWWWW"))
