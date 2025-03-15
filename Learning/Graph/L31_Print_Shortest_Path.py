from sortedcontainers import SortedSet
from math import inf

class Solution:
    def print_shortest_path(self, adj_list, src, dest):
        n = len(adj_list)
        dist = [inf for _ in range(n)]
        dist[src] = 0

        parent = [i for i in range(n)]
        parent[src] = 0
        
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
                    parent[conn] = node
                    node_set.add((conn,dist[conn]))
        print(parent)

        path = []
        temp = dest
        while temp != src:
            path.append(temp)
            temp = parent[temp]
        path.append(src)
        
        return path[::-1]



adj_list = [[(1, 2), (4, 1)], [(2, 3)], [(3, 6)], [], [(5, 4), (2, 2)], [(3, 1)]]
print(adj_list)
print(Solution().print_shortest_path(adj_list,src=0, dest = 5))
