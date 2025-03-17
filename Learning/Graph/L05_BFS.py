from collections import deque

class Solution:
    def bfs(self, adj_list, source):
        visited_arr = [0] * (len(adj_list) + 1)
        q = deque()
        q.append(source)
        visited_arr[source] = 1
        level = 0

        while len(q):
            level_arr = []

            for _ in range(len(q)):
                node = q.popleft()
                
                for conn in adj_list[node]:
                    if not visited_arr[conn]:
                        q.append(conn)
                        visited_arr[conn] = 1
                
                level_arr.append(node)
            print(level,level_arr)
            level += 1


adj_list = {1: [2, 3, 4], 2: [1, 4], 4: [5, 2, 1], 5: [4, 3], 3: [1, 5]}
adj_list = {1: [2, 5], 2: [1, 5,3], 4: [3, 5,], 5: [1,2, 4, 3], 3: [2,4, 5]}
source = 1

Solution().bfs(adj_list, source)