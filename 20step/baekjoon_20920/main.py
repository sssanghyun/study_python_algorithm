import sys

N, M = map(int, sys.stdin.readline().split())
d = {}

for _ in range(N):
    s = sys.stdin.readline().rstrip()

    if len(s) >= M:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
d = sorted(d.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in d:
    print(i[0])