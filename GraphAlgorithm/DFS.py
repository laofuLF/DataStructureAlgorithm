# DFS Traverse Algorithm
from collections import defaultdict


# Adjacency list is used to store the graph
class Graph:

    def __init__(self):

        # create a default dictionary to store graph
        self.graph = defaultdict(list)

    # a function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A function to help do the recursive process for DFS
    def DFS_help(self, v, visited):

        # Mark the starting vertex as visited

        visited[v] = True
        print(chr(v + ord("A")), end=" ")

        # Recurse through all unvisited node
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_help(i, visited)

    # main dfs function with input of starting vertex v and the number of total vertices n
    def DFS(self, v, n):

        # Mark all the vertices as not visited
        visited = [False] * n

        # print DFS traversal
        number = ord(v) - ord('A')
        self.DFS_help(number, visited)



# Test:
# Create a graph and add all the edges in the graph
g = Graph()

#  edges are represent ed in numbers :['AB', 'AD', 'AI', 'BD', 'BC', 'BE', 'CE', 'CF', 'DE', 'DG',
#           'EF', 'EG', 'EH', 'FH', 'GH', 'GI', 'GJ', 'HJ', 'IJ']  with A = 0 and J = 9
edges = [[0, 1], [0, 3], [0, 8], [1, 2], [1, 3], [1, 4], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5],
         [4, 6], [4, 7], [5, 7], [6, 7], [6, 8], [6, 9], [7, 9], [8, 9]]
for edge in edges:
    g.add_edge(edge[0], edge[1])

# print DFS search result with starting index 0 and total number of vertices 10
g.DFS("A", 10)
