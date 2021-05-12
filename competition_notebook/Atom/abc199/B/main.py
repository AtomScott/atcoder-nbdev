#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]"):
    count = 0
    for x in range(1, 1001):
        ok = False
        for a, b in zip(A,B):
            if not (a <= x <= b):
                ok = True
        if not ok:
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
