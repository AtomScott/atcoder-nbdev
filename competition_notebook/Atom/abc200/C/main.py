#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]"):
    Ad = defaultdict(int)
    count = 0
    for i, a in enumerate(A[::-1]):
        idx = a%200
        Ad[idx]+= 1
        count += Ad[idx]
    print(count-N)
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

#         if i == 0:
#             Ad[N-i-1][a % 200]+= 1
#         else:
#             Ad[N-i-1] = {k:v for k,v in Ad[N-i].items()}
#             Ad[N-i-1][a % 200]+= 1
            
        
        
#     for d in Ad:
#         print(sum(d.values()))
#     count = 0
#     for i, a in enumerate(A):
#         count += Ad[i][a%200] 
#         print(Ad[i][a%200])
        
#     A_max, A_min = [], []
#     for i, a in enumerate(A[::-1]):
#         if i == 0:
#             A_max.append(a)
#             A_min.append(a)
#         else:
#             if A_max[i-1] < a:
#                 A_max.append(a)
#             else:
#                 A_max.append(A_max[i-1])
#             if A_min[i-1] > a:
#                 A_min.append(a)
#             else:
#                 A_min.append(A_min[i-1])
    
#     A_max = A_max[::-1]
#     A_min = A_min[::-1]
#     print(A_max, A_min)
#     count = 0
#     for i, ai in enumerate(A):
#         for j, aj in enumerate(A[i+1:]):
            
#             if ai - aj % 200 == 0:
#                 count += 1
#             if 


