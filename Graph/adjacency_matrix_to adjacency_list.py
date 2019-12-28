# Convert an unweighted undirected graph edges from adjacency matrix to list with starting index 1
from collections import defaultdict


def matrix_to_list(matrix):
    graph = defaultdict(list)

    # Enumerate list from index of 1, eliminate 0s
    for i, v in enumerate(matrix, 1):
        for j, u in enumerate(v, 1):
            if u != 0:
                graph[i].append(j)
    return graph


# Test code
matrix = [[0, 1, 1, 1],
          [1, 0, 1, 1],
          [1, 1, 0, 0],
          [1, 1, 0, 0]]

g = matrix_to_list(matrix)
print(g)
