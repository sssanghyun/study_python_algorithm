import sys

N = int(sys.stdin.readline())

arr = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0:
        arr[i] = 0
    elif i == 1:
        arr[i] = 1
    else:
        arr[i] = arr[i-2] + arr[i-1]

print(arr[-1])