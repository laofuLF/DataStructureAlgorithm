# Convert an adjacency list to incidence matrix
# Time complexity is O(n*m)


def adjacency_list_to_incidence_matrix(adj_list):
    number_of_edges = 0
    edges = []
    for i, v in enumerate(adj_list, 1):
        for j, u in enumerate(adj_list[i]):
            edge = [i, adj_list[i][j]]
            edge_swap = [adj_list[i][j], i]
            if edge_swap not in edges:
                edges.append(edge)

    width, height = int(len(edges)), len(adj_list)
    Matrix = [[0 for x in range(width)] for y in range(height)]

    for i in range(len(edges)):
        v1, v2 = edges[i]
        Matrix[v1 - 1][i] = 1
        Matrix[v2 - 1][i] = 1

    return Matrix


# Help print the matrix in a better format
def print_help(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


# Test code
adj_list = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2], 4: [1, 2]}
matrix = adjacency_list_to_incidence_matrix(adj_list)
print_help(matrix)