def graph_adj_matrix(n, m, edges):
    mat = [[0 for _ in range(n+1)] for _ in range(n+1)]
    print(mat)
    for u, v in edges:
        mat[u][v], mat[v][u] = 1,1
    print(mat)
    return mat

nodes = 5
edge = 6
edges = [(1,2), (4,5), (1,3), (3,5), (2,4), (1,4)]
mat = graph_adj_matrix(nodes, edge, edges)
for _ in mat:
    print(_)

# SC -> O(N*N)
# Without weights:
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0]
[0, 1, 0, 0, 1, 0]
[0, 1, 0, 0, 0, 1]
[0, 1, 1, 0, 0, 1]
[0, 0, 0, 1, 1, 0]

# with weights:
[0, 0, 0, 0, 0, 0]
[0, 0, 4, 2, 14, 0]
[0, 4, 0, 0, 1, 0]
[0, 2, 0, 0, 0, 1]
[0, 14, 1, 0, 0, 9]
[0, 0, 0, 1, 9, 0]