import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
d = deque([str(i) for i in range(1, N+1)])
result = []

while len(d) != 0:
    for i in range(K):
        if i == K-1:
            result.append(d.popleft())
        else:
            d.append(d.popleft())
print("<"+', '.join(result)+">")