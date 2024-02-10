import sys

N, M = map(int, sys.stdin.readline().split())

str_N = set()
str_M = set()
count = 0
for _ in range(N):
    str_N.add(sys.stdin.readline().strip())
for _ in range(M):
    if sys.stdin.readline().strip() in str_N:
        count += 1

print(count)