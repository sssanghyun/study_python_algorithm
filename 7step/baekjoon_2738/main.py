import sys

N, M = map(int, sys.stdin.readline().split())
A = list()
B = list()
for i in range(N*2):
    if i < N:
        A.append(list(map(int, sys.stdin.readline().split())))
    elif i >= N:
        B.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end= ' ')
    print()