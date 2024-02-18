import sys

N, M, R = map(int, sys.stdin.readline().split(' '))
node = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
sys.setrecursionlimit(N+10)
for i in range(M):
    u, v = map(int, sys.stdin.readline().split(' '))
    node[u].append(v)
    node[v].append(u)

for i in range(1, N+1):
    node[i].sort(key=lambda x: -x)
count = 0
def dfs(r):
    global count
    count += 1
    visited[r] = count
    for i in node[r]:
        if not visited[i]:
            dfs(i)
dfs(R)

for i in range(1, N+1):
    print(visited[i])