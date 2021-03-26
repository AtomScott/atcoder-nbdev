#!/usr/bin/env python3
import sys


def solve(K: int):    
    x  = 0
    for i in range(1, K+1):
        if not (x := (x*10+7) % K):
            print(i)
            return
    print(-1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()
