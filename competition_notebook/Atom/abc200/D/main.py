#!/usr/bin/env python3
import sys
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import numpy as np

MOD = 200  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str

def pascals_triangle(n):
    triangle = []
    for line in range(1, n + 1):
        C = 1
        row = []
        for i in range(1, line + 1):
            row.append(C)
            C = int(C * (line - i) / i)
        triangle.append(row)
    return triangle

def solve(N: int, A: "List[int]"):
    A = A[:9]
    A = A[::-1]

    depth = len(A) - 1
    T = nx.binomial_tree(depth)
    n_nodes = len(T.nodes)
    n_nodes_on_row = pascals_triangle(depth+1)[depth]
    
    row = []
    depth = 1
    
    T.nodes[0]['value'] = A[0]
    for i, edge in enumerate(nx.bfs_edges(T, depth)):
        row.append(edge)
        
        if len(row) >= n_nodes_on_row[depth]:
            for p, c in row[::-1]:
                T.nodes[c]['value'] = (T.nodes[p]['value'] + A[c%len(A)]) % 200 

            depth += 1
            row = []
        

    pos = graphviz_layout(T, prog="dot")
    nx.draw_networkx(T, pos, with_labels=True)
    plt.show()
    
    for data in T.nodes.data():
        print(data)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
