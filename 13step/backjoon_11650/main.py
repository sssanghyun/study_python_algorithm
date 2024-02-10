import sys

arr = [[] for row in range(200001)]

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr[x+100000].append(y)

for i in range(len(arr)):
    if len(arr[i]) != 0:
        arr[i].sort()
        for j in arr[i]:
            print(i-100000, j)