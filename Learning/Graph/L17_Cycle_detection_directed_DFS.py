# Important to keep visited and path visited to make sure that cycle is found in the same path.

class Solution:
    def detect_cycle(self, adj_list):
        n = len(adj_list)
        # Zero-indexed
        visited_array = [0] * n
        path_visited_array = [0] * n

        def dfs_cycle(source):
            print(f"dfs{source}")
            for conn in adj_list[source]:
                # Check if already visited  
                if visited_array[conn]:
                    # and in the same path 
                    if path_visited_array[conn]:
                        print(f"dfs{conn}")
                        return True
                    # else:
                    #     return False
                else:        
                    # If not, call dfs
                    visited_array[conn] = 1
                    path_visited_array[conn] = 1
                    if dfs_cycle(conn) == True:
                        return True
                    else:
                        path_visited_array[conn] = 0
            return False

        # Important for components
        for i in range(1,n):
            if not visited_array[i]:
                visited_array[i] = 1
                path_visited_array[i] = 1
                if dfs_cycle(i) == True:
                    return True
        return False

adj_list1 = {
    0: [1],
    1: [2], 
    2: [3], 
    3: [4,7], 
    4: [5],
    5: [6],
    6 : [],
    7 :[5],
    8: [9],
    9: [10],
    10: [8]
}


adj_list2 = {
    0: [1],
    1: [2], 
    2: [3], 
    3: [4], 
    4: [5],
    5: [7,6],
    6 : [],
    7 :[3],
    8: [9],
    9: [10],
    10: [8]
}
print(Solution().detect_cycle(adj_list=adj_list1))
print(Solution().detect_cycle(adj_list=adj_list2))