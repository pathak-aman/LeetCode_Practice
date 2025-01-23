from collections import defaultdict
from typing import List

# For theory, check the notion notes.

class Solution:
    def dfs(self, source):
        self.visited_arr[source] = 1

        for node in self.adj_list[source]:
            if not self.visited_arr[node]:
                self.dfs(node)
    
    def convert_adjacency_matrix(self, isConnected):
        n = len(isConnected)
        self.adj_list = defaultdict(list)
        for i in range(0,n):
            for j in range(0, n):
                if isConnected[i][j] == 1 and not i == j:
                    self.adj_list[i+1].append(j+1)
                    # self.adj_list[j+1].append(i+1)
        print(self.adj_list)
        return n

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = self.convert_adjacency_matrix(isConnected)
        self.visited_arr = [0] * (n + 1)
        provences = 0
        for i in range(1, len(self.visited_arr)):
            if not self.visited_arr[i]:
                provences += 1
                self.dfs(i)    
        return provences



isConnected = [[0,1,1,1,1,0],[0,0,0,0,1,0],[1,0,1,1,0,1],[0,0,0,0,0,1],[1,0,0,0,0,1],[0,1,0,0,0,1]]
print(Solution().findCircleNum(isConnected))