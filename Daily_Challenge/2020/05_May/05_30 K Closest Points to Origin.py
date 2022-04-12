from math import sqrt
import operator
class Solution:
    def kClosest(self, points, K):
        absolute = abs
        kClosestPoints = points[:K]
        kClosestDistance = [sqrt(point[0]**2 + point[1]**2) for point in kClosestPoints]
        indexMaxDistace, maxKClosestDistance = max(enumerate(kClosestDistance), key=operator.itemgetter(1))
        for remainingPoint in points[K:]:
            if not max(absolute(remainingPoint[0]),absolute(remainingPoint[1])) > maxKClosestDistance:
                print(remainingPoint,maxKClosestDistance,indexMaxDistace)
obj1 = Solution()
obj1.kClosest([[3,3],[5,-1],[-2,4]], K = 2)