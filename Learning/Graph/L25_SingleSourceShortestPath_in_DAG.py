# Shortest path in Directed Acyclic Graph from a source

# Step 1: TopoSort
# Step 2: dist[src] = 0 and edge releaxation
# This Processing the vertices in topological order ensures that by the time you get to a vertex, you've already processed all the vertices that can precede it which reduces the computation time significantly. 
# In this approach, we traverse the nodes sequentially according to their reachability from the source.

from math import inf

class Solution:
    def topo_sort(self, source, adj_list):
        self.visited[source] = 1
        for node, wt in adj_list[source]:

            if not self.visited[node]:
                self.topo_sort(node, adj_list)
        self.stack.append(source)

    def SSSP(self, N, edges, start):

        adj_list = [[] for i in range(N)]
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adj_list[u].append((v, wt))
        print(adj_list)
        
        # Step 1: Topo sort -> Since DAG no cycles.
        self.n = len(adj_list)
        self.visited = [0 for i in range(self.n)]
        self.stack = []
        for i in range(self.n):
            if not self.visited[i]:
                self.topo_sort(i, adj_list)
        print(self.stack)

        # Step 2: Edge relaxation
        dist = [inf for i in range(self.n)]
        dist[start] = 0

        while self.stack:
            src = self.stack.pop()
            for node, wt in adj_list[src]:
                dist[node] = min(dist[node], dist[src] + wt)

        return dist


N = 6
edges= [(0,1,2),(0,4,1),(4,5,4),(4,2,2),(1,2,3),(2,3,6),(5,3,1)]

print(Solution().SSSP(N, edges, 4))

