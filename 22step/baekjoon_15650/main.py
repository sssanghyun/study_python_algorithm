# 참고 https://jiwon-coding.tistory.com/22
import sys

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(start, N+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(i+1)
        s.pop()
        # print(s)
        # print(visited)
        visited[i] = False

N, M = map(int, sys.stdin.readline().split())

s = []
visited = [False] * (N+1)

dfs(1)