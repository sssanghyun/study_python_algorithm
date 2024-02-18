import sys
import heapq

hq = []

N = int(sys.stdin.readline())

for _ in range(N):
    a = int(sys.stdin.readline())

    if a == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, a)