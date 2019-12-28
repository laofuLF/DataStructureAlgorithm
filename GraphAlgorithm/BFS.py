# BFS graph traverse algorithm
from collections import defaultdict


class Graph:

    def __init__(self):

        # create a default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of the graph
    def BFS(self, s, n):

        # Mark all the vertices as not visited
        visited = [False] * n

        # Create a queue for BFS
        queue = []

        # Mark the starting vertex as visited and store in a queue
        number = ord(s) - ord('A')
        queue.append(number)
        visited[number] = True

        while queue:

            # Pop a value from queue
            number = queue.pop(0)
            print(chr(number + ord("A")), end=" ")

            for i in self.graph[number]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


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
g.BFS("A", 10)
