import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
pq = PriorityQueue(maxsize=N)
for _ in range(N):
    a = int(sys.stdin.readline())

    if a == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((-(a), a))