class Solution:
    def detect_cycle(self, adj_list):
        n = len(adj_list)
        # Zero-indexed
        visited_array = [0] * n

        def dfs_cycle(source, parent):
            print(f"dfs{source, parent}")
            for conn in adj_list[source]:
                # Check if already visited    
                if not visited_array[conn]:
                    # If not, call dfs
                    visited_array[conn] = 1
                    dfs_cycle(conn, source)
            
                
                # If visited, check if its someone other than parent
                elif conn != parent:
                    print(source, parent, conn)
                    print("cycle found!")
                    return True
            return False

        for i in range(n):
            if not visited_array[i]:
                visited_array[i] = 1
                cycle_found = dfs_cycle(i, -1)
                if cycle_found:
                    return cycle_found
        return False

adj_list1 = {
    0: [1],
    1: [0,2,4], 
    2: [1,3], 
    3: [2,4], 
    4: [1,3]
}

adj_list2 = {
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

adj_list3 = {
    0: [2, 3, 4], 
    2: [0], 
    4: [1, 0], 
    1: [4], 
    3: [0]
}

print(Solution().detect_cycle(adj_list=adj_list2))