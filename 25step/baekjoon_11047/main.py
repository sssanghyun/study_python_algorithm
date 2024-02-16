import sys

N, K = map(int, sys.stdin.readline().split(' '))
coin = [0 for _ in range(N)]

for i in range(N):
    coin[i] = int(sys.stdin.readline())

count = 0

for i in range(N-1, -1, -1):
    if K >= coin[i]:
        count += K // coin[i]
        K = K % coin[i]
print(count)