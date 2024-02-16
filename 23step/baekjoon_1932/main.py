import sys

N = int(sys.stdin.readline())
arr = [[0]] * N

for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split(' ')))

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            arr[i][j] = arr[i-1][j] + arr[i][j]
        elif j == i:
            arr[i][j] = arr[i-1][-1] + arr[i][j]
        else:
            arr[i][j] = max(arr[i-1][j-1], arr[i-1][j]) + arr[i][j]

print(max(arr[-1]))