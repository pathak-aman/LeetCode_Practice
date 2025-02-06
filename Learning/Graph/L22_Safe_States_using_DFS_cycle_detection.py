class Solution:
    def cycle_detection_dfs(self, source, graph):
        print(f"dfs{source}")


        for conn in graph[source]:
            if not self.visited[conn]:
                self.visited[conn] = 1
                self.path_visited[conn] = 1
                if self.cycle_detection_dfs(conn, graph):
                    
                    return True

            else:
                if self.path_visited[conn]:
                    return True
                
        # If code reaches here, that means, for our source all the paths have been checked and they aren't associated with cycle        
        self.path_visited[source] = 0
        self.states[source] = 1
        return False        


    def eventualSafeNodes(self, graph):
        self.n = len(graph)
        self.visited = [0] * self.n
        self.path_visited = [0] * self.n
        self.states = [0] * self.n

        for i in range(self.n):
            if not self.visited[i]:
                self.visited[i] = 1
                self.path_visited[i] = 1
                self.cycle_detection_dfs(i, graph)
        return [i for i in range(self.n) if self.states[i] == 1]

graph = [[1,2],[2,3],[5],[0],[5],[],[]]


print(Solution().eventualSafeNodes(graph))