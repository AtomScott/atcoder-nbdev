#!/usr/bin/env python3
import sys


def solve(X: int, K: int, D: int):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(X, K, D)

if __name__ == '__main__':
    main()
