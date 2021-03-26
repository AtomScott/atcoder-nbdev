#!/usr/bin/env python3
# %%writefileと#!の間の行が入らないように注意！

import sys
from math import sqrt
from itertools import combinations

def solve(N: int, D: int, X: "List[int]", Y: "List[int]"):
    count = 0
    
    for x,y in zip(X,Y):
        if sqrt((x)**2 + (y)**2) <= D:
            count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, D, X, Y)

if __name__ == '__main__':
    main()
