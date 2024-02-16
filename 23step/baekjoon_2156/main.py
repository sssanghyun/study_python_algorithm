import sys

n = int(sys.stdin.readline())
w = [0 for _ in range(n)]
dp = [0 for _ in range(10001)]

for i in range(n):
    w[i] = int(sys.stdin.readline())

dp[1] = w[0]

if n >= 2:
    dp[2] = w[0] + w[1]

for i in range(3, n+1):
    dp[i] = max(dp[i-1], w[i-1] + w[i-2] + dp[i-3], w[i-1] + dp[i-2])

print(dp[n])