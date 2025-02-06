# **Intuition**: We get this pattern *- “This comes before that”,* this should ring a bell. Topological sort.
from collections import deque

class Solution:
    def topo_sort(self,K):
        
        q = deque()
        topo_order = []
        for i in range(K):
            if not self.indegree[i]:
                q.append(i) 
        
        while len(q):
            letter = q.popleft()
            topo_order.append(letter)

            for conn in self.adj_list[letter]:
                self.indegree[conn] -= 1
                if self.indegree[conn] == 0:
                    q.append(conn)
        
        return topo_order

    def compare_and_make_graph(self, s1, s2):
        for ch_1, ch_2 in zip(s1,s2):
            if ch_1 != ch_2:
                # ch_1 becomes before ch_2, edge ch_1 -> ch_2 exist. 
                # Increase indegree of ch_2 
                self.indegree[ord(ch_2) - ord("a")] += 1
                self.adj_list[ord(ch_1) - ord("a")].append(ord(ch_2) - ord("a") )
                break


    def alien_dict(self, N, K, dict_words):
        self.indegree = [0 for i in range(K)]
        self.adj_list = [[] for i in range(K)]

        for i in range(N-1):
            self.compare_and_make_graph(dict_words[i], dict_words[i+1]) 

        topo_order = self.topo_sort(K)    
        return "".join([chr(ord("a") + i) for i in topo_order])

N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]
print(Solution().alien_dict(N,K,dict))

N = 3
K = 3
dict = ["caa","aaa","aab"]

print(Solution().alien_dict(N,K,dict))