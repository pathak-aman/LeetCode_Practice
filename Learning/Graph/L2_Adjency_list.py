from collections import defaultdict

def graph_adj_list(n, m, edges):
    adj_dict = defaultdict(list)
    for u, v in edges:
        adj_dict[u].append(v)
        adj_dict[v].append(u)
    return adj_dict

nodes = 5
edge = 6
edges = [(1,2), (4,5), (1,3), (3,5), (2,4), (1,4)]
adj_dict = graph_adj_list(nodes, edge, edges)
print(adj_dict)

# SC -> O(2*E)