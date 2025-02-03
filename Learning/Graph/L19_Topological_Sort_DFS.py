class Solution:
    def dfs(self, i, adj_list):
        print(f"dfs{i}")

        for conn in adj_list[i]:
            if not self.visited[conn]:
                self.visited[conn] = 1
                self.dfs(conn, adj_list)

        self.stack.append(i)


    def topological_sort_dfs(self, adj_list):
        self.n = len(adj_list)
        self.visited = [0] * self.n
        self.stack = []

        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = 1
                self.dfs(i, adj_list)

        return self.stack[::-1]
    
adj_list = [[],[3],[3],[],[0,1],[0,2]]
print(Solution().topological_sort_dfs(adj_list))