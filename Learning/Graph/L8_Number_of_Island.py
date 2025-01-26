class Solution:
    def bfs(self, source):
        pass

    def dfs(self,grid,i,j):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for x, y in zip(dx,dy):
            xt, yt = i + x, j + y
            if 0 <= xt < self.m and 0 <= yt < self.n and (not self.visited[xt][yt]) and grid[xt][yt] == "1":
                self.visited[xt][yt] = 1
                self.dfs(grid,xt,yt)



    def numIslands(self, grid):
        self.m, self.n = len(grid), len(grid[0])
        islands = 0
        self.visited = [[0 for i in range(self.n)] for j in range(self.m)]
        print(self.visited)
        for i in range(self.m):
            for j in range(self.n):
                print(not self.visited[i][j] and grid[i][j])
                if (not self.visited[i][j]) and grid[i][j] == "1":
                    print("GO DFS")
                    islands +=1
                    self.visited[i][j] = 1
                    self.dfs(grid,i,j)
                    print(self.visited)
                    # self.bfs(i,j)
        return islands



grid =[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] 
print(Solution().numIslands(grid))