import sys

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()

N, M = map(int, sys.stdin.readline().split())

s = []

dfs(1)