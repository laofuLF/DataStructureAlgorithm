# Convert an incidence matrix to adjacency list
# Time complexity is O(n*m)
from collections import defaultdict


def incidence_matrix_to_adjacency_list(matrix):
    adj_list = defaultdict(list)

    number_of_edges = len(matrix[0])
    for i in range(number_of_edges):
        count = 0
        j = 0
        while count < 2:    # Using while loop to reduce redundant iteration
            if matrix[j][i] == 1 and count == 0:
                count += 1
                v1 = j + 1  # increment all vertices by 1 so that the first vertex is 1
            elif matrix[j][i] == 1 and count == 1:
                count += 1
                v2 = j + 1
            j += 1
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    return adj_list


# Test code
inc_matrix = [[1, 1, 1, 0, 0],
             [1, 0, 0, 1, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 1, 0, 1]]

adjacency_list = incidence_matrix_to_adjacency_list(inc_matrix)
print(adjacency_list)
