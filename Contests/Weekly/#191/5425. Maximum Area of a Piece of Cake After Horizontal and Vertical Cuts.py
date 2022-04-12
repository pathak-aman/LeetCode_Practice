class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        horizontalCuts = [0]+sorted(horizontalCuts)+[h]
        verticalCuts = [0]+sorted(verticalCuts)+[w]

        print(horizontalCuts,verticalCuts)
        max_diff_horizontal,max_diff_verticle = 0,0
        for i in range(len(horizontalCuts)-1):
            diff_h = horizontalCuts[i+1]-horizontalCuts[i]
            print(diff_h)
            if diff_h>max_diff_horizontal:
                max_diff_horizontal=diff_h


        for j in range(len(verticalCuts) - 1):
            diff_v = verticalCuts[j+1]-verticalCuts[j]
            print(diff_v)
            if diff_v>max_diff_verticle:
                max_diff_verticle=diff_v

        return max_diff_verticle*max_diff_horizontal


obj1 = Solution()
print(obj1.maxArea( h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))

