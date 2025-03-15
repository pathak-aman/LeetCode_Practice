# Inituition - Djikstra's 
# Need to keep popping minimum efforts
# Need to check while popping if we are at the destination, then no other path exist with less efforts


from collections import deque
from math import inf

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)
        src = (0,0)
        dest = (n-1,n-1)
        distance = [[inf for _ in range(n)] for _ in range(n)]

#       (distance, (x,y))
        q = deque()
        q.append((0, (0,0)))

        delx = [0, +1, 0, -1]
        dely = [+1, 0, -1, 0]
        
        while q:
            dist, (x, y) = q.popleft()
            for dx, dy in zip(delx, dely):
                x_new, y_new = x + dx, y + dy

                if 0 <= x_new < n and 0 <= y_new < n and grid[x_new][y_new] == 1 and dist + 1 < dist[x_new][y_new]:
                    dist[x_new][y_new] = dist+ 1
                    q.append((dist+ 1, (x_new, y_new)))

                    if dest == (x_new, y_new):
                        return dist + 1
        return -1
    




   
