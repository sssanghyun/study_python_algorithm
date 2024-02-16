# 참고 https://velog.io/@minchoul2/%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98-Python
import sys

N = int(sys.stdin.readline())
dp = [[0] * 10 for _ in range(N)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N-1]) % 1_000_000_000)