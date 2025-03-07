# Inituition: Use min -heap and distance array

from math import inf
import heapq

class Solution:
    def Dijkstra(self, adj_list, src):

        n = len(adj_list)
        dist = [inf for _ in range(n)]
        dist[src] = 0
        min_heap = []
        # [distance, node]
        print(dist)
        heapq.heappush(min_heap, [0,src])

        while min_heap:
            print(min_heap)
            distance, node = heapq.heappop(min_heap)
            for conn, wt in adj_list[node]:
                if dist[conn] > distance + wt:
                    dist[conn] = distance + wt
                    heapq.heappush(min_heap, [dist[conn], conn])
        return dist

    
adj_list = [[(1, 2), (4, 1)], [(2, 3)], [(3, 6)], [], [(5, 4), (2, 2)], [(3, 1)]]
print(adj_list)
print(Solution().Dijkstra(adj_list,src=0))


            



    
