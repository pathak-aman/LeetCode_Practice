from collections import deque

class Solution:
    def detect_cycle(self, adj_list):
        n = len(adj_list)
        # Zero-indexed
        visited_array = [0] * n

        def bfs_cycle(source, adj_list):
            q = deque()
            q.append((source, -1))

            while len(q):
                for _ in range(len(q)):
                    node, parent = q.popleft()
                    for conn in adj_list[node]:
                        if not visited_array[conn]:
                            visited_array[conn] = 1
                            q.append((conn, node))

                        # If a conncetion is visited and is not a parent, therefore cycle!    
                        elif conn != parent:
                            print(node, parent, conn)
                            # Cycle detected!
                            print("cycle detected!")
                            return True
            return False

        for i in range(n):
            if not visited_array[i]:
                visited_array[i] = 1
                cycle_found = bfs_cycle(i, adj_list)
                if cycle_found:
                    return cycle_found
        return False
                
adj_list = {
    0: [1],
    1: [0,2,4], 
    2: [1,3], 
    3: [2,4], 
    4: [1,3]
}

adj_list = {
    0:[1,2],
    1:[0,3],
    2:[0,4],
    3:[1],
    4:[2,5,6],
    5:[4],
    6:[4],
    7:[8,9],
    8:[7,9],
    9:[7,8]
}

# adj_list = {
#     0: [2, 3, 4], 
#     2: [0], 
#     4: [1, 0], 
#     1: [4], 
#     3: [0]
# }

print(Solution().detect_cycle(adj_list=adj_list))