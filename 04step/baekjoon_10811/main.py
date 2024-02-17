import sys

N, M = map(int, sys.stdin.readline().split())
l = list(i for i in range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if not i-j == 0:
        temp = l[i-1:j]
        temp.reverse()
        count = 0
        for k in range(i-1, j):
            l[k] = temp[count]
            count += 1

print(*l)