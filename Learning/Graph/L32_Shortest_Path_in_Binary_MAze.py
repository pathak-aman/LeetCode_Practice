# Inituition - Djikstra's, edge wt is 1. No need of using PQ, Queue is enough, as weights are one.

from collections import deque
from math import inf

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        dest = (n-1,n-1)
        distance = [[inf for _ in range(n)] for _ in range(n)]

#       (distance, (x,y))
        q = deque()
        q.append((0, (0,0)))

        delx = [0, +1, 0, -1]
        dely = [+1, 0, -1, 0]
        
        while q:
            curr_dist, (x, y) = q.popleft()
            for dx, dy in zip(delx, dely):
                x_new, y_new = x + dx, y + dy

                if 0 <= x_new < n and 0 <= y_new < n and grid[x_new][y_new] == 1 and curr_dist + 1 < distance[x_new][y_new]:
                    distance[x_new][y_new] = curr_dist+ 1
                    q.append((curr_dist+ 1, (x_new, y_new)))

                    if dest == (x_new, y_new):
                        return curr_dist + 1
        return -1
    




   
