import sys

N, M = map(int, sys.stdin.readline().split())
l = list(0 for i in range(N))

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i, j+1):
        l[idx-1] = k

print(*l)
