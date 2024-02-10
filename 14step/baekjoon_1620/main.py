import sys

N, M = map(int, sys.stdin.readline().split())
mon = {}

for i in range(1, N+1):
    str = sys.stdin.readline().strip()
    mon[i] = str
    mon[str] = i

for _ in range(M):
    q = sys.stdin.readline().strip()
    if q in mon:
        print(mon.get(q))
    else:
        print(mon.get(int(q)))