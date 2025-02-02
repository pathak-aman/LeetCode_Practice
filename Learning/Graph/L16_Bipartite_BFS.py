from collections import deque

class Solution:
    def check_BFS(self, graph, source):
        q = deque([source])

        while len(q):
            for _ in range(len(q)):
                node = q.popleft()
                for adj in graph[node]:
                    if self.coloured[adj] == -1:
                        self.coloured[adj] = 1 - self.coloured[node]
                        q.append(adj)
                    elif self.coloured[adj] == self.coloured[node]:
                        return False
        return True
                        
    def isBipartite(self, graph) -> bool:
        self.n = len(graph) # Vertices
        self.coloured = [-1 for i in range(self.n)]
        
        for i in range(self.n):
            if self.coloured[i] == -1:
                self.coloured[i] = 0
                if self.check_BFS(graph, i) == False:
                    return False
        return True


graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# graph = [[1,3],[0,2],[1,3],[0,2]]

print(Solution().isBipartite(graph))