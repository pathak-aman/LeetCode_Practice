from collections import deque

class Solution:
    def kahn_bfs(self, adj_list):
        self.ans = []
        q = deque()
        for i in range(self.n):
            if not self.indegree[i]:
                q.append(i)
            
        while len(q):
            node = q.popleft()
            self.ans.append(node)
            for conn in adj_list[node]:
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:
                    q.append(conn)
    
    def get_indegrees(self,adj_list):
        indegree = [0] * self.n
        for edges in adj_list:
            for edge in edges:
                indegree[edge] += 1
        return indegree

    def topological_sort_bfs_kahn(self, adj_list):
        self.n = len(adj_list)
        self.indegree = self.get_indegrees(adj_list)

        self.kahn_bfs(adj_list)
        return self.ans

    
adj_list = [[],[3],[3],[],[0,1],[0,2], [], [], []]
print(Solution().topological_sort_bfs_kahn(adj_list))