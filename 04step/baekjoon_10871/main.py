import sys

N, X = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
result = list()
for i in l:
    if i < X:
        result.append(i)
print(*result)