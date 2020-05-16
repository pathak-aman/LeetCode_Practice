class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        startPos =(sr,sc)
        oldColor = image[sr][sc]
        allOldColor = [(i,j) for i in range(len(image)) for j in range(len(image[i])) if image[i][j] == oldColor]
        allOldColor.remove(startPos)
        toBeColored = [startPos]

        print(allOldColor)
        print(toBeColored)
        for i in toBeColored:
            # j = 0
            # while j < len(allOldColor):
            for j in allOldColor:
                if abs(i[0]-j[0])==1 and abs(i[1]-j[1])==0 or \
                        abs(i[0]-j[0])==0 and abs(i[1]-j[1])==1:
                    allOldColor.remove(j)
                    toBeColored.append(j)
                # if abs(i[0]-allOldColor[j][0])==1 and abs(i[1]-allOldColor[j][1])==0 or \
                #         abs(i[0]-allOldColor[j][0])==0 and abs(i[1]-allOldColor[j][1])==1:
                #     allOldColor.remove(allOldColor[j])
                #     toBeColored.append(allOldColor[j])
                # j+=1


        for allPoints in toBeColored:
            image[allPoints[0]][allPoints[1]] = newColor

        return image


obj1 = Solution()
print(obj1.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]],sr =1, sc = 1,newColor=2))


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image