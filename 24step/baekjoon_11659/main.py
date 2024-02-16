import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
s = [[0] for _ in range(N)]
s[0] = arr[0]
for i in range(1, N):
    s[i] = arr[i] + s[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split(' '))
    if i == 1:
        print(s[j - 1])
    else:
        print(s[j - 1] - s[i - 2])