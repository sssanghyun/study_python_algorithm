import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split(' '))
node = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
q = deque()

for i in range(M):
    u, v = map(int, sys.stdin.readline().split(' '))
    node[u].append(v)
    node[v].append(u)

for i in range(1, N+1):
    node[i].sort()
count = 1

visited[R] = count
q.append(R)

while len(q) > 0:
    a = q.popleft()
    for k in node[a]:
        if visited[k] == 0:
            count += 1
            visited[k] = count
            q.append(k)

for i in range(1, N+1):
    print(visited[i])