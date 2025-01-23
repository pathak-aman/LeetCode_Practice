from collections import deque

class Solution:
    def dfs_helper(self, adj_list, source):
        print(source)
        self.visited_arr[source] = 1
        
        for node in adj_list[source]:
            if not self.visited_arr[node]:
                
                self.dfs_helper(adj_list, node)
        
        
    def dfs(self, adj_list, source):
        self.visited_arr = [0] * (len(adj_list) + 1)
        self.dfs_helper(adj_list, source) 

adj_list = {1: [2, 3, 4], 2: [1, 4], 4: [5, 2, 1], 5: [4, 3], 3: [1, 5]}
adj_list = {1: [2, 5], 2: [1, 5,3], 4: [3, 5,], 5: [1,2, 4, 3], 3: [2,4, 5]}
source = 1

Solution().dfs(adj_list, source)