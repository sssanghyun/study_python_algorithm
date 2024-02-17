import sys

N, M = map(int, sys.stdin.readline().split(' '))
A = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

M, K = map(int, sys.stdin.readline().split(' '))
B = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for k in range(K):
        for j in range(M):
            C[i][k] += A[i][j] * B[j][k]

for i in range(len(C)):
    for j in range(len(C[i])):
        print(C[i][j], end=' ')
    print()