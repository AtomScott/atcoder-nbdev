#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, c: "List[int]", l: "List[int]", r: "List[int]"):
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    c = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, Q, c, l, r)

if __name__ == '__main__':
    main()
