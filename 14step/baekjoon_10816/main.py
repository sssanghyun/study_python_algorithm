import sys

card = [0 for _ in range(-10000000, 10000001)]
N = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))

for v in arr_n:
    card[v] += 1

for v in arr_m:
    print(card[v], end=' ')