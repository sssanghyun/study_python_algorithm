# 참고 https://www.youtube.com/watch?v=5Lu34WIx2Us&t=1612s
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split(' ')))
dp = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))