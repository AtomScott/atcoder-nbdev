#!/usr/bin/env python3
# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
        
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 

# Function to check if it is safe to assign color `c` to vertex `v`
def isSafe(graph, color, v, c):
    color = tuple(color)
    if seen.get(color):
        return False
    else:
        seen[color]=True
        return 
    # check the color of every adjacent vertex of `v`
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
 
    return True
 

def kColorable(g, color, k, v, N, count):
 
    # if all colors are assigned, print the solution
    if v == N:
        count += 1
        return count
 
    # try all possible combinations of available colors
    for c in range(1, k + 1):
        # if it is safe to assign color `c` to vertex `v`
        if isSafe(g, color, v, c):
            # assign color `c` to vertex `v`
            color[v] = c
 
            # recur for the next vertex
            count = kColorable(g, color, k, v + 1, N, count)
            print(color)
            # backtrack
            color[v] = 0
    return count 
 
global seen 
seen = {}
if __name__ == '__main__':
  
    # A list to store colors (10–colorable graph)
    COLORS = ["", "R", "G", 'B']
 
    # Set number of vertices in the graph
    N, M = list(map(int, input().split()))
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
        edges[i][0] -= 1
        edges[i][1] -= 1
 
    # build a graph from the given edges
    g = Graph(edges, N)
 
    k = 3
 
    color = [None] * N
 
    # print all k–colorable configurations of the graph
    count = kColorable(g, color, k, 0, N, 0)
    print(count)
