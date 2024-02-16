# 참고 https://alpyrithm.tistory.com/134
import sys

N = int(sys.stdin.readline())
km = list(map(int, sys.stdin.readline().split(' ')))
cost = list(map(int, sys.stdin.readline().split(' ')))
result = 0
cur_cost = cost[0]

for i in range(N-1):
    if cost[i] < cur_cost:
        cur_cost = cost[i]
    result += cur_cost * km[i]

print(result)