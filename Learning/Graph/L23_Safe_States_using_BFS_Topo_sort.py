from collections import deque

class Solution:

    def topo_sort(self):
        self.states = [0 for i in range(self.n)]
        q = deque ()
        for vertex in range(self.n):
            if not self.indegree[vertex]:
                q.append(vertex)

        while len(q):
            node = q.popleft()
            self.states[node] = 1
            for conn in self.rev_graph[node]:
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:
                    q.append(conn)


    def eventualSafeNodes(self, graph):
        self.n = len(graph)
        self.rev_graph = [[]  for i in range(self.n)]

        for in_vertex in range(self.n):
            for out_vertex in graph[in_vertex]:
                self.rev_graph[out_vertex].append(in_vertex)

        self.indegree = [0 for i in range(self.n)]
        for edges in self.rev_graph:
            for edge in edges:
                self.indegree[edge] += 1

        self.topo_sort()
        return [i for i in range(self.n) if self.states[i] == 1]
        

graph = [[1,2],[2,3],[5],[0],[5],[],[]]


print(Solution().eventualSafeNodes(graph))