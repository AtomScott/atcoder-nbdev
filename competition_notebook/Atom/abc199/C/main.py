#!/usr/bin/env python3


def main(N, S, Q, T, A, B):
    # Failed to predict input format
    S1 = list(S[:N])
    S2 = list(S[N:])
    flip = False
    
    for t, a, b in zip(T, A, B):
        if t == 1:
            a -= 1
            b -= 1
            if a < N and b < N:
                S1[a], S1[b] = S1[b], S1[a]
            elif a < N and b >= N:
                S1[a], S2[b-N] = S2[b-N], S1[a]
            elif a >= N and b < N:
                S1[a-N], S2[b] = S2[N], S1[a-N]
            else:
                S2[a-N], S2[b-N] = S2[b-N], S2[a-N]
        else:
            S1, S2 = S2, S1
            
#         print(S1, S2)
#             flip=not flip
#         print(t,a, b, S1+S2)
#     if flip:
#         print(''.join(S1+S2))
#     else:
#         print(''.join(S2+S1))
    print(''.join(S1+S2))
    pass

if __name__ == '__main__':
    N = int(input())
    S = input()
    Q = int(input())
    T, A, B = [], [], []
    for i in range(Q):
        t, a, b = list(map(int, input().split()))
        T.append(t)
        A.append(a)
        B.append(b)
    main(N, S, Q, T, A, B)
