# We apply topo sort as we can clearly notice the need of linear ordering.
from collections import deque

class Solution:
    def topo_sort(self, numCourses, adj_list):
        self.topo_order = []
        q = deque()
        for i in range(numCourses):
            if not self.indegree[i]:
                q.append(i)
        
        while len(q):
            node = q.popleft()
            self.topo_order.append(node)
            for conn in adj_list[node]:
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:
                    q.append(conn)


    def canFinish(self, numCourses: int, prerequisites):
        adj_list = [[] for i in range(numCourses)]
        self.indegree = [0] * numCourses
        for in_vertex, out_vertex in prerequisites:
            adj_list[out_vertex].append(in_vertex)
            self.indegree[in_vertex] += 1
        
        print(adj_list, self.indegree)
        self.topo_sort(numCourses, adj_list)

        if len(self.topo_order) < numCourses:
            return False
        else:
            return True


2 
[[1,0]]
2
[[1,0],[0,1]]
5
[[1,4],[2,4],[3,1],[3,2]]
6
[[1,0],[1,2],[3,1],[2,3],[2,4],[4,5],[2,5]]
numCourses = 6
prerequisites = [[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]]
print(Solution().canFinish(numCourses, prerequisites))
