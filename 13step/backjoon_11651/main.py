import sys

arr = [[] for row in range(200001)]

N = int(sys.stdin.readline())

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr[y+100000].append(x)

for i in range(len(arr)):
    if len(arr[i]) != 0:
        arr[i].sort()
        for j in arr[i]:
            print(j, i-100000)