
# Create basic graph class to perform DFS.
from collections import defaultdict
from .edge import Edge

class Graph():

    def __init__(self):
        self.graph = defaultdict(list);

    def addEdge(self, start, end):
        self.graph[start].append(end)

    def createGraph(self, edges):
        for edge in edges:
            # Convert the node letters to numbers and add edges
            node1 = ord(edge.vertice_1) - 65
            node2 = ord(edge.vertice_2) - 65
            # Add edge in both directions, as this is an undirected graph
            self.addEdge(node1, node2)
            self.addEdge(node2, node1)

    def DFS(self, edgeList, start, numberOfNodes):
        visited = [0] * (numberOfNodes)

        g = self.createGraph(edgeList)
        startNode = ord(start) - 65
        self.recursiveDFS(startNode, visited)
        
        return visited

    def recursiveDFS(self, j, visited):
        # Mark node as visited
        visited[j] = 1
        for i in self.graph[j]:
            if(visited[i] == 0):
                self.recursiveDFS(i, visited)