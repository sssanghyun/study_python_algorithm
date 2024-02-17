import sys

N, K = map(int, sys.stdin.readline().split())
result = []

for i in range(1, N+1):
    if N % i == 0:
        result.append(i)

    if len(result) == K:
        break
try:
    if result[K-1]:
        print(result[K-1])
except:
    print(0)