import sys

N, M = map(int, sys.stdin.readline().split())
arr_n = set()
arr_m = set()
for _ in range(N):
    arr_n.add(sys.stdin.readline().strip())

for _ in range(M):
    arr_m.add(sys.stdin.readline().strip())

result = arr_n & arr_m
result = list(result)
result.sort()
print(len(result))

for r in result:
    print(r)