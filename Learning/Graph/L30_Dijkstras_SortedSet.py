from sortedcontainers import SortedSet
from math import inf

class Solution:
    def dijkstra(self, adj_list, src):
        n = len(adj_list)
        dist = [inf for _ in range(n)]
        dist[src] = 0
        
        node_set = SortedSet()
        node_set.add((src, 0))

        while node_set:
            # logn
            node, distance = node_set.pop(0)

            for conn, wt in adj_list[node]:
                if distance + wt < dist[conn]:
                    if (conn, dist[conn]) in node_set:
                        node_set.remove((conn, dist[conn]))
                    # logn    
                    dist[conn] = distance + wt
                    node_set.add((conn,dist[conn]))
        return dist



adj_list = [[(1, 2), (4, 1)], [(2, 3)], [(3, 6)], [], [(5, 4), (2, 2)], [(3, 1)]]
print(adj_list)
print(Solution().dijkstra(adj_list,src=0))
