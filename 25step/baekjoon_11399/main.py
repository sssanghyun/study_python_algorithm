import sys

N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split(' ')))
p.sort()

d = [0 for _ in range(N)]
d[0] = p[0]
for i in range(1, N):
    d[i] = d[i-1] + p[i]

print(sum(d))